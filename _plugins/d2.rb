require 'digest/md5'
require 'fileutils'
require 'open3'

module Jekyll
  module D2Renderer
    CACHE_DIR = '.d2_cache'.freeze
    CODE_FENCE_REGEX = /```d2\s*([\s\S]*?)```/m.freeze

    class << self
      def available?
        return @available unless @available.nil?

        @available = system('command', '-v', 'd2', out: File::NULL, err: File::NULL)
        Jekyll.logger.warn('D2', 'd2 CLI not found, leaving diagrams unprocessed.') unless @available
        @available
      end

      def process(doc)
        content = doc.content
        return unless content&.include?('```d2')
        return unless available?

        doc.content = content.gsub(CODE_FENCE_REGEX) do
          diagram = Regexp.last_match(1).to_s.strip
          next Regexp.last_match(0) if diagram.empty?

          begin
            svg = render(diagram, doc.site)
            %(<div class="d2-diagram">#{svg}</div>)
          rescue StandardError => e
            identifier = doc.respond_to?(:relative_path) ? doc.relative_path : doc.path
            Jekyll.logger.warn('D2', "Failed to render diagram in #{identifier}: #{e.message}")
            Regexp.last_match(0)
          end
        end
      end

      private

      def cache_dir(site)
        @cache_dirs ||= {}
        @cache_dirs[site.source] ||= begin
          dir = File.join(site.source, CACHE_DIR)
          FileUtils.mkdir_p(dir)
          dir
        end
      end

      def render(code, site)
        cache = cache_dir(site)
        hash = Digest::MD5.hexdigest(code)
        svg_path = File.join(cache, "#{hash}.svg")

        unless File.exist?(svg_path)
          tmp_path = File.join(cache, "tmp-#{hash}.d2")
          File.write(tmp_path, code)
          stdout, stderr, status = Open3.capture3('d2', tmp_path, svg_path, '--pad', '10')
          FileUtils.rm_f(tmp_path)

          unless status.success?
            FileUtils.rm_f(svg_path)
            message = stderr.empty? ? stdout : stderr
            raise "d2 CLI exited with #{status.exitstatus}: #{message.strip}"
          end
        end

        File.read(svg_path)
      end
    end
  end
end

Jekyll::Hooks.register :documents, :pre_render do |doc|
  Jekyll::D2Renderer.process(doc)
end

Jekyll::Hooks.register :pages, :pre_render do |page|
  Jekyll::D2Renderer.process(page)
end
