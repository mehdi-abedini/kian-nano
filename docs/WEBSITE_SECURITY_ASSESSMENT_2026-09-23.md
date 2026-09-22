# Kian Nano Karno Website - Security & Operational Baseline
Date: 2026-09-23
Target: https://nanokarno.ir

Verified: WordPress 7.0.6; PHP 8.3.33; OceanWP 4.0.6; Elementor 4.3.0 active; Elementor Pro 3.32.2 inactive; WPVibe 1.17.4; Imunify Security 4.1.0; LiteSpeed Cache 6.5.4; WPML 4.6.13; WPForms 1.6.3; Hide My WP Ghost 6.0.22; Easy Updates Manager Premium 9.0.13.

Mobile Lighthouse: Performance 69, Accessibility 96, Best Practices 96, SEO 92. Performance LCP 6.6s/FCP 3.2s. Issues: unused JS (~297 KiB), unused CSS (~94 KiB), contrast, low-resolution images, invalid robots.txt.

Security findings:
1. Hide My WP Ghost 6.0.22 is materially outdated; current public vulnerability records list fixes in 7.0.x for unauthenticated SSRF/open redirect and firewall/URL-hiding bypasses.
2. WPML 4.6.13 is outdated; current records show SQL-injection fixes in 4.9.6 and later 4.9.x releases.
3. WPForms 1.6.3 dates to 2020 and is far behind current releases.
4. Easy Updates Manager is blocking normal update flow, increasing patch latency risk.
5. WordPress 7.0.6 is current in the 7.0 branch, but 7.1.2 is the current actively maintained release family.

Core checksum verification: 3,501 core files verified with no mismatches/missing files, but unexpected files were detected inside wp-admin/wp-includes (mostly error_log paths). These require host-level identification before declaring the installation clean.

Decision: do not add a second heavyweight security plugin yet. Imunify Security is already active. First remediate existing outdated components, inspect Imunify configuration/logs, verify a restorable backup, then reassess.

Production plugin/theme/core changes remain human-approval gated.
