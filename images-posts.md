# Images Used As Top Post Image

Generated on 2026-03-01 02:02:59 -0500 from post front matter `image` fields.

- Total files under `/images`: **240**
- Posts with `image` metadata: **118**
- Local `/images/...` references: **116**
- Unique local images referenced: **116**
- External image references: **2**
- Local references missing files: **1**

## How to Use This File

Use this file as the single source of truth for top-image tracking and recommendations.

### Scope Rules

1. Track only post front matter `image` usage.
2. Treat local images as paths starting with `/images/`.
3. Keep external image URLs in `## External Image References`.
4. Do not mix inline-content images with top-image metadata usage.

### Recommendation Rules

1. Recommend images using **filename relevance + pixel size only**.
2. Do not perform visual/content analysis of image pixels.
3. Prefer unused local images for recommendations.
4. Keep recommendations in `### Pending Recommendations`.
5. Each pending recommendation row should include:
   - post path,
   - suggested image path,
   - size,
   - status,
   - short filename-based reason.

### Apply Rules

1. When a recommendation is accepted and applied to a post:
   - update that post front matter first,
   - ensure the image appears in `## Local \`/images\` References`,
   - remove the row from `### Pending Recommendations`.
2. Remove applied images from any “unused/future” lists.

### Validation Rules

1. Verify summary counts match table contents.
2. Verify each local image path exists on disk; if not, list under `## Missing Local Image Files`.
3. If the user asks to use an image, reflect that state change immediately in:
   - post front matter,
   - local references,
   - pending/applied recommendation sections.

### Behavior Rule For Future Requests

On future “recommend/apply top image” requests, always follow this sequence:

1. apply or update post front matter as requested,
2. regenerate this file,
3. confirm that pending/applied/unused sections are consistent with the new state.

## Local `/images` References

| Image Path | Post(s) |
| --- | --- |
| `/images/autumn-leaves.jpg` | `_posts/2018/2018-10-24-a-test-page-for-iis-cpu-throttling.md` |
| `/images/autumn-tree.jpg` | `_posts/2018/2018-10-17-shifting-to-azure-app-service-on-linux.md` |
| `/images/bell-center.jpg` | `_posts/2019/2019-4-29-samsung-net-core-debugger-and-monodevelop.md` |
| `/images/biosphere-montreal.jpg` | `_posts/2018/2018-2-7-offline-publishing-asp-net-core-apps.md` |
| `/images/birds-over-lake-tommy-thompson-park.jpg` | `_posts/2021/2021-5-18-dotnet-framework-lifecycle-changes.md` |
| `/images/blue-2011.jpg` | `_posts/2011/2011-1-2-i-love-the-blue-colour.md` |
| `/images/brookfield-place-entrance.jpg` | `_posts/2021/2021-4-24-microsoft-web-administration-of-iis-express.md` |
| `/images/buddhist-statue.jpg` | `_posts/2018/2018-8-5-how-to-use-private-repos-as-submodules-in-vsts.md` |
| `/images/bund-xuhui.jpg` | `_posts/2017/2017-12-13-snmp-pro-the-upcoming-2-0-release.md` |
| `/images/canada-flag.jpg` | `_posts/2019/2019-4-6-net-core-rpms-for-centos.md` |
| `/images/canada-maltage.jpg` | `_posts/2018/2018-9-6-the-very-common-mistakes-when-using-iis-url-rewrite-module.md` |
| `/images/canada-place-vancouver.jpg` | `_posts/2024/2024-3-31-running-next-js-web-apps-on-iis-with-httpplatformhandler.md` |
| `/images/canadiens-montreal.jpg` | `_posts/2020/2020-5-6-the-challenges-to-enable-open-with-windows-terminal.md` |
| `/images/canal-bridge.jpg` | `_posts/2018/2018-8-7-replacing-zapier-with-azure-function.md` |
| `/images/cannons.jpg` | `_posts/2018/2018-3-15-what-tool-to-write-restructuredtext-the-war-is-over.md` |
| `/images/chilly-day-city-hall-toronto.jpg` | `_posts/2024/2024-6-18-classic-asp-on-windows-server-2025.md` |
| `/images/cibc-square-after-rain.jpg` | `_posts/2026/2026-03-01-snmp-library-v13-from-v12-to-dotnetsnmp.md` |
| `/images/city-hall-toronto.jpg` | `_posts/2018/2018-9-19-wildcard-host-name-support-in-old-iis-releases.md` |
| `/images/cleaning-telus-building.jpg` | `_posts/2025/2025-07-26-a-brief-history-of-net-core-winforms-designer.md` |
| `/images/cloud-reflection-mississauga.jpg` | `_posts/2021/2021-4-1-the-end-of-mono.md` |
| `/images/clouds-canal.jpg` | `_posts/2018/2018-7-28-the-rough-history-of-referenced-assemblies.md` |
| `/images/clouds-over-lake.jpg` | `_posts/2021/2021-1-22-monodevelop-source-code-licensing.md` |
| `/images/clouds-over-woods.jpg` | `_posts/2020/2020-4-14-how-to-replace-backgroundworker-with-async-await-and-tasks.md` |
| `/images/cloudy-day-montreal.jpg` | `_posts/2019/2019-7-1-the-basic-facts-about-iis-asp-net-process-thread-identities.md` |
| `/images/cn-tower-dark-clouds.jpg` | `_posts/2024/2024-12-21-httpplatformhandler-windows-authentication-tips.md` |
| `/images/cn-tower-reflection-delta-hotel.jpg` | `_posts/2023/2023-5-22-vscode-iis-extension-for-sphinx-users.md` |
| `/images/cn-tower-shadow.jpg` | `_posts/2024/2024-4-8-httpplatformhandler-v2.md` |
| `/images/cn-tower-sunset.jpg` | `_posts/2023/2023-9-10-how-to-use-antlr-4-on-net-in-2023.md` |
| `/images/cn-tower-through-glass-raindrop.jpg` | `_posts/2023/2023-4-7-the-rough-history-of-iis-httpplatformhandler.md` |
| `/images/columbia-university.jpg` | `_posts/2018/2018-4-15-secrets-behind-jetbrains-rider-and-iis-express.md` |
| `/images/competitiveness-prosperity.jpg` | `_posts/2020/2020-3-11-how-i-set-up-visual-studio-code-remote-with-multipass-on-macos.md` |
| `/images/construction-site.jpg` | `_posts/2019/2019-5-20-brief-history-of-monodevelop.md` |
| `/images/crossroad-wellington.jpg` | `_posts/2018/2018-12-6-locate-msbuild-via-powershell-on-different-operating-systems.md` |
| `/images/desktop-runtime.png` | `_posts/2025/2025-11-30-recover-missing-dotnet-msi-on-windows-with-wix-toolset.md` |
| `/images/doves-at-dufferin-mall.jpg` | `_posts/2023/2023-1-12-history-of-this-blog.md` |
| `/images/doves-over-roy-thomson-hall.jpg` | `_posts/2024/2024-2-9-running-go-web-apps-on-iis-with-httpplatformhandler.md` |
| `/images/doves-sunset.jpg` | `_posts/2018/2018-11-19-vscode-restructuredtext-extension-synchronized-preview-support.md` |
| `/images/downtown-montreal.jpg` | `_posts/2020/2020-6-1-migrating-files-uwp-to-uno-part-i.md` |
| `/images/downtown-view-from-fort-york.jpg` | `_posts/2023/2023-3-31-successful-and-failed-attempt-my-first-pull-request-for-asp-net-core.md` |
| `/images/dundas-street-toronto.jpg` | `_posts/2023/2023-1-29-how-to-step-into-net-core-source-code-in-vs-code.md` |
| `/images/ey-building-toronto.jpg` | `_posts/2023/2023-1-16-running-nuxt-3-web-apps-on-iis-with-httpplatformhandler.md` |
| `/images/flight-canada.jpg` | `_posts/2019/2019-4-22-asp-net-core-diagnostics-for-iis-iis-express-stories-behind.md` |
| `/images/flight-landing-over-ontario-lake.jpg` | `_posts/2024/2024-4-5-running-nest-web-apps-on-iis-with-httpplatformhandler.md` |
| `/images/flight-toward-asia.jpg` | `_posts/2024/2024-10-9-github-actions-workflow-upgrade-issues.md` |
| `/images/four-seasons-boston.jpg` | `_posts/2018/2018-4-22-snmp-library-gaps-filled-in-snmp-v3-support.md` |
| `/images/glass-ceiling-cleaner.jpg` | `_posts/2020/2020-12-13-the-rough-history-of-microsoft-reference-source.md` |
| `/images/go-station-outside-toronto.jpg` | `_posts/2022/2022-12-27-obfuscar-question-on-local-variables.md` |
| `/images/goose-canal.jpg` | `_posts/2018/2018-9-2-yet-another-official-launch-of-lextudio.md` |
| `/images/grass-sun.jpg` | `_posts/2018/2018-8-5-how-to-abort-cancel-a-build-in-vsts.md` |
| `/images/highway-407-station-inside.jpg` | `_posts/2022/2022-12-8-new-preview-engine-from-bosch.md` |
| `/images/highway-407-station-outside.jpg` | `_posts/2022/2022-11-8-sharp-snmp-new-release-net-6.md` |
| `/images/hiking-day-birds.jpg` | `_posts/2024/2024-9-19-hosting-multiple-versions-of-sphinx-documentation.md` |
| `/images/home-2011.jpg` | `_posts/2011/2011-1-2-somewhere-called-home.md` |
| `/images/hong-kong-habour.jpg` | `_posts/2022/2022-11-8-asmspy-on-artifacts-verifcation.md` |
| `/images/iced-canal.jpg` | `_posts/2020/2020-3-23-how-to-install-microsoft-cors-module-for-iis-express.md` |
| `/images/ikea-montreal.jpg` | `_posts/2019/2019-2-2-a-wix-installer-example-jexus-manager.md` |
| `/images/jexus-manager.jpg` | `_posts/2018/2018-10-11-new-screenshot-of-jexus-manager.md` |
| `/images/lady-in-red-cineplex-dundas.jpg` | `_posts/2022/2022-7-10-running-flask-web-apps-on-iis-with-httpplatformhandler.md` |
| `/images/lake-side-rc-harris-water-treatment-plant.jpg` | `_posts/2022/2022-6-11-running-nodejs-web-apps-on-iis-with-httpplatformhandler.md` |
| `/images/lake-view-from-rc-harris-water-treatment-plant.jpg` | `_posts/2022/2022-5-8-powershell-on-macos.md` |
| `/images/le-village-olympique.jpg` | `_posts/2019/2019-6-17-things-you-should-know-about-windows-cache-extension-for-php.md` |
| `/images/leaves-glen-rd-bridge.jpg` | `_posts/2024/2024-3-30-running-fastapi-web-apps-on-iis-with-httpplatformhandler.md` |
| `/images/lights-with-red-background.jpg` | `_posts/2025/2025-03-24-invoke-win32-api-nodejs-libwin32-koffi.md` |
| `/images/linus-bikes.jpg` | `_posts/2018/2018-3-21-update-on-offline-publishing-asp-net-core-apps.md` |
| `/images/love-park-toronto.jpg` | `_posts/2024/2024-3-30-running-django-web-apps-on-iis-with-httpplatformhandler.md` |
| `/images/marriage-place.jpg` | `_posts/2020/2020-12-18-integration-with-snooty-language-server.md` |
| `/images/meizu-2010.jpg` | `_posts/2010/2010-10-20-meizu-my.md` |
| `/images/mont-royal.jpg` | `_posts/2018/2018-12-8-migrating-jexus-manager-to-net-core-3-0.md` |
| `/images/msdn.png` | `_posts/2016/2016-4-1-build-2016.md` |
| `/images/neighborhood-bellevue.jpg` | `_posts/2024/2024-3-16-pysnmp-and-home-assistant.md` |
| `/images/new-td-building.jpg` | `_posts/2026/2026-02-28-obfuscar-3-0-from-2-2-to-srm.md` |
| `/images/new-year-decoration-toronto.jpg` | `_posts/2023/2023-1-14-public-sessions-programs-I-worked-on-in-the-past.md` |
| `/images/night-montreal.jpg` | `_posts/2018/2018-3-9-make-obfuscar-a-global-tool-in-net-core.md` |
| `/images/night-street.jpg` | `_posts/2018/2018-8-25-everything-good-and-horrible-about-powershell-gallery.md` |
| `/images/oct-pujiang.jpg` | `_posts/2017/2017-12-22-how-to-use-antlr-4-on-net-in-2017.md` |
| `/images/office-lights-downtown-toronto.jpg` | `_posts/2025/2025-11-22-getting-started-python-uv-windows.md` |
| `/images/pavillion-e-ets.jpg` | `_posts/2019/2019-8-14-the-rough-history-of-net-core-debuggers.md` |
| `/images/place-des-canotiers.jpg` | `_posts/2018/2018-6-19-second-update-on-offline-publishing-asp-net-core-apps.md` |
| `/images/project-rover-preview.png` | `_posts/2026/2026-01-02-project-rover-keeping-ilspy-wpf-and-rover-avalonia-ui-in-sync.md` |
| `/images/purple-hearts-over-aquarium.jpg` | `_posts/2024/2024-9-22-esbonio-vs-code-reviewers-guide.md` |
| `/images/py1-pyramid.jpg` | `_posts/2020/2020-1-20-unpleasant-facts-about-hangfire.md` |
| `/images/railway-bridge.jpg` | `_posts/2018/2018-10-6-my-understanding-of-the-visual-studio-2017-2019-announcement.md` |
| `/images/rainy-day-union-station.jpg` | `_posts/2024/2024-10-10-websockets-is-unsupported-error.md` |
| `/images/reader-on-kew-balmy-beach.jpg` | `_posts/2022/2022-2-27-new-language-server-and-case-study.md` |
| `/images/riverside.jpg` | `_posts/2020/2020-8-19-the-end-of-monodevelop.md` |
| `/images/rush-hours-union-station.jpg` | `_posts/2025/2025-06-21-experimental-recycleonfilechange-httpplatformhandler.md` |
| `/images/s-3rd-st.jpg` | `_posts/2018/2018-3-31-why-you-should-forget-php-manager-for-iis.md` |
| `/images/seattle-public-library.jpg` | `_posts/2019/2019-11-22-the-horrible-facts-on-visual-studio-setup-projects.md` |
| `/images/snow-ladder.jpg` | `_posts/2018/2018-6-15-the-horrible-story-of-publishing-net-core-web-apps-for-beginners.md` |
| `/images/st-john.jpg` | `_posts/2018/2018-7-2-jexus-manager-update-july-2018.md` |
| `/images/st-lawrence-river.jpg` | `_posts/2018/2018-3-30-what-should-you-check-when-visual-studio-cannot-debug-asp-net-core-project.md` |
| `/images/summer-canal.jpg` | `_posts/2018/2018-8-5-ci-cd-pipeline-with-vsts-and-zapier.md` |
| `/images/summer-flowers-university-avenue.jpg` | `_posts/2025/2025-07-15-simplest-python-windows-get-started.md` |
| `/images/summer-sunset-over-td-building.jpg` | `_posts/2021/2021-11-26-how-i-ended-up-with-vscode-as-git-client.md` |
| `/images/sunny-ontario-lake.jpg` | `_posts/2024/2024-6-22-brief-guide-to-windows-arm64-developers.md` |
| `/images/sunset-clouds-toronto.jpg` | `_posts/2021/2021-9-12-different-ways-to-create-vscode-extension-dependencies.md` |
| `/images/sunset-near-long-branch.jpg` | `_posts/2024/2024-8-31-mono-project-history-future-analysis.md` |
| `/images/sunset-over-cn-tower.jpg` | `_posts/2025/2025-08-28-hosting-aspnetcore-nativeaot-on-iis-with-httpplatformhandler.md` |
| `/images/sunset-reflections.jpg` | `_posts/2024/2024-10-29-history-of-snmpsharpnet.md` |
| `/images/telus-garden.jpg` | `_posts/2020/2020-5-13-miseries-around-asp-net-windows-authentication-setup.md` |
| `/images/tree-branches.jpg` | `_posts/2019/2019-3-1-two-years-on-medium.md` |
| `/images/tree-reflection.jpg` | `_posts/2019/2019-5-8-what-does-net-5-mean-to-you.md` |
| `/images/trees-moon.jpg` | `_posts/2018/2018-7-29-signing-your-code-for-the-good-and-the-bad.md` |
| `/images/trees-old-port.jpg` | `_posts/2018/2018-8-5-self-hosting-sphinx-sites-on-azure-app-service.md` |
| `/images/vancouver-convention-center.jpg` | `_posts/2020/2020-5-5-everything-you-might-need-about-iis-server-header.md` |
| `/images/view-from-tommy-thompson-park-toronto.jpg` | `_posts/2025/2025-03-14-understanding-port-configuration-in-httpplatformhandler.md` |
| `/images/view-woodbine-beach.jpg` | `_posts/2021/2021-9-4-asp-net-core-crashes-and-burns.md` |
| `/images/washington-monument.jpg` | `_posts/2018/2018-7-27-snmp-library-bouncy-castle-extensions.md` |
| `/images/wellington-ann.jpg` | `_posts/2018/2018-8-2-history-of-php-manager-for-iis.md` |
| `/images/whalers-cove-bellevue.jpg` | `_posts/2024/2024-9-15-reviving-pysnmp.md` |
| `/images/winter-branches.jpg` | `_posts/2019/2019-3-2-snmp-library-11-0-and-above.md` |
| `/images/winter-trees-2.jpg` | `_posts/2019/2019-4-12-the-cost-of-open-source-solutions-a-case-study-on-red-hat-and-docker.md` |
| `/images/winter-trees-3.jpg` | `_posts/2018/2018-3-9-behind-the-scene-of-net-core-global-tools.md` |
| `/images/winter-trees.jpg` | `_posts/2020/2020-4-30-remote-management-of-containerized-iis-instances-on-windows-server-core.md` |
| `/images/wires-tower-north-toronto.jpg` | `_posts/2021/2021-8-28-dockpanel-suite-3.1.0-release.md` |
| `/images/xp-metro.jpg` | `_posts/2010/2010-6-14-windows-shanghai-metro.md` |

## External Image References

| Image URL | Post |
| --- | --- |
| `https://github.com/lextudio/ProjectRover/raw/master/images/social.png` | `_posts/2025/2025-12-22-dotnet-timeline-and-project-rover.md` |
| `https://github.com/lextudio/dotuninstall/raw/main/social-preview.png` | `_posts/2025/2025-09-26-the-dotnet-uninstall-story.md` |

## Missing Local Image Files

| Missing Path | Post(s) |
| --- | --- |
| `/images/project-rover-preview.png` | `_posts/2026/2026-01-02-project-rover-keeping-ilspy-wpf-and-rover-avalonia-ui-in-sync.md` |

## Curated Unused Images (Filename + Size Only)

Selection rule for this section:

- Content relevance judged by **filename only**.
- Size judged by stored pixel dimensions only (no visual analysis).

### Pending Recommendations

- None at the moment.

### Remaining Good Unused Images For Future Posts

| Image Path | Size | Filename-Based Theme |
| --- | ---: | --- |
| `/images/net-standard.png` | `1024x580` | .NET/SRM-related technical post |
| `/images/net-foundation.png` | `1024x577` | .NET ecosystem / platform evolution |
| `/images/python-announcement.png` | `1280x777` | language/tooling announcement style |
| `/images/antlr-rider.jpg` | `1400x735` | developer tooling / IDE |
| `/images/rst-vscode.png` | `1400x737` | editor/tooling |
| `/images/jekyll-now-theme-screenshot.jpg` | `1146x1098` | blogging/docs tooling |
| `/images/flickr.jpg` | `1082x767` | web/content theme |
| `/images/xamarin.png` | `1166x722` | .NET mobile/cross-platform history |
| `/images/bash.png` | `1024x575` | CLI/scripting topic |
| `/images/hololens.png` | `1024x574` | Microsoft/innovation topic |
| `/images/cryengine.png` | `1024x574` | engine/performance topic |
| `/images/game.png` | `1024x572` | software/game tooling topic |

### Topic-Specific But Small (Keep As Backup)

| Image Path | Size | Note |
| --- | ---: | --- |
| `/images/obfuscar-global-tool.png` | `560x344` | Highly relevant filename, but relatively small as a top image. |
| `/images/obfuscar-global-tool-folder.png` | `450x180` | Relevant filename, but banner is small and narrow. |
| `/images/obfuscar-in-ilspy.png` | `258x106` | Relevant filename, but too small for hero usage. |
| `/images/snmp-mono-android.png` | `320x196` | Relevant filename, but small legacy resolution. |
