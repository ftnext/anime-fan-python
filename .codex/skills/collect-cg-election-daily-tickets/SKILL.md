---
name: collect-cg-election-daily-tickets
description: Collect daily voting tickets for the Idolmaster Cinderella Girls general election portal. Use when the user asks Codex to automate, check, or finish today's daily ticket collection for シンデレラガール総選挙2026 / Cinderella Girls election missions on idolmaster-official.jp and ASOBI STORE, especially 日次 or デイリーミッション ticket collection. Scope is daily tickets only; non-daily tickets, purchases, serial-code entry, physical check-ins, and other one-off missions are explicitly out of scope.
---

# Collect CG Election Daily Tickets

## Operating Rules

Use the user's existing Chrome session, because the workflow depends on logged-in ASOBI STORE and Idolmaster Portal state. Start with ASOBI STORE, then continue to Idolmaster Portal. Do not handle passwords, OTPs, account settings, payment, purchase, or identity-link setup. If ASOBI STORE shows a guest/login state, first try the existing-session login recovery described below; ask the user only when that recovery cannot continue without credentials, OTP, CAPTCHA, account confirmation, account settings, or other user-only input. If Idolmaster Portal is not logged in, ask the user to log in unless an already-signed-in Bandai Namco ID continuation is clearly available without entering credentials or changing account state.

Only automate daily voting-ticket missions. Treat a mission as in scope only when its card is explicitly marked with `デイリーミッション`, `ログインボーナス（1日1回）`, `1日1回`, or equivalent daily wording. Skip anything categorized or described as:

- `あいことば`, serial code, or `シリアルコード`
- `チェックイン` or physical spot check-in
- store/product purchase, ticket purchase, event ticket, stream ticket, or paid action
- cumulative view-count milestones, basic-mission count rewards, premium purchase missions, or `その他`
- any `プレミアムミッション` that is not clearly a daily login bonus

Prefer semantic UI targets from the accessibility tree or visible labels. Avoid coordinate-only replay unless there is no usable label.

Do not optimize playback timing to influence YouTube or other external engagement metrics. Use video playback only to satisfy and verify the Idolmaster Portal daily mission.

Separate the two Idolmaster Portal pages by purpose:

- Use `https://idolmaster-official.jp/cinderellagirls/vote2026/vote` to receive tickets from missions that are already cleared.
- Use `https://idolmaster-official.jp/cinderellagirls/vote2026/vote/mission` to perform or open daily mission challenges.

After completing a daily mission from `/vote/mission`, return to `/vote` to receive the ticket. Do not rely on `/vote/mission` as the primary receive page.

## Workflow

1. Open Chrome to `https://shop.asobistore.jp/` first. Wait for the ASOBI STORE page to finish loading, because this may satisfy the related daily mission on the Idolmaster Portal side.
2. Verify ASOBI STORE login from the visible account state. If the store shows `こんにちは ゲスト様`, `ログイン/新規登録`, or equivalent guest state, click the ASOBI STORE login entry and then select `バンダイナムコIDでログイン` if shown. If an already-signed-in Bandai Namco ID session redirects back to ASOBI STORE and the page shows a named account such as `こんにちは ...様`, continue. If the flow asks for email, password, OTP, CAPTCHA, account registration, profile/address input, account-link setup, or any account confirmation beyond choosing an already-signed-in Bandai Namco ID login path, stop and ask the user to complete it. Do not operate account or payment flows.
3. Open `https://idolmaster-official.jp/cinderellagirls/vote2026`.
4. Verify Idolmaster Portal login by looking for `ログイン中`, the profile menu, or the My Desk area. If absent, ask the user to log in.
5. Open `https://idolmaster-official.jp/cinderellagirls/vote2026/vote`.
6. Record the visible current ticket count if available (`現在の所持投票券数`) so the final report can say whether it changed.
7. On `/vote`, receive tickets for already-cleared daily/login-style missions:
   - `ASOBI STOREプレミアム会員専用 ログインボーナス（1日1回）`
   - `アイドルマスター ポータルにログイン`, when presented as a daily/current reward
   Click `受け取る` only when it belongs to one of these daily/login cards and is enabled.
8. For each click, verify a toast or page update such as `投票券を N 枚 受け取りました！`. If a receive button becomes disabled, treat that card as collected.
9. Open `https://idolmaster-official.jp/cinderellagirls/vote2026/vote/mission` to perform daily missions. Work through only cards marked `デイリーミッション`.
10. On `/vote/mission`, use eligible `チャレンジ` links to perform the mission. If a daily card already appears cleared or says `投票券を受け取れます`, do not receive it there first; go back to `/vote` and receive it from the vote page.
11. For Music Series daily viewing challenges, use these recorded stable targets:
   - `総選挙特設サイトで 『アイドルコミュ毎日更新』の動画を視聴`: open the `チャレンジ` link to `/cinderellagirls/vote2026/musicseries`; start the relevant embedded video if one is visible.
   - `シンデレラNo.1` MV: open `/musicseries?tab=mv_lyrics`, select the `シンデレラNo.1 ... ver.` image/title, then click `動画を再生` when the YouTube embed appears.
   - `ROSE ～禁じられた愛～` MV: open `/musicseries?tab=mv_lyrics#mv-2`, select `第2弾「ROSE ～禁じられた愛～」`, then click `動画を再生` when needed.
12. For any embedded video, confirm playback has started, wait only long enough for the Idolmaster mission state to update or for a reasonable page-level completion signal, then close the video modal/tab or navigate back. Do not replay or wait a fixed duration solely to affect external view counts.
13. After each daily mission action, open `/vote`, reload if needed, and receive any newly enabled daily ticket there. Verify `投票券を N 枚 受け取りました！` or that the receive button becomes disabled.
14. Return to `/vote/mission` only to look for remaining eligible daily `チャレンジ` tasks. Repeat the mission-page action and vote-page receive cycle until no in-scope daily challenge remains and `/vote` has no enabled in-scope `受け取る`.

## ASOBI STORE Handling

Always open `https://shop.asobistore.jp/` before Idolmaster Portal work. The goal is only to establish the logged-in ASOBI STORE session that can clear daily login-style missions.

If ASOBI STORE shows a guest state, attempt this narrow existing-session recovery before asking the user:

1. Click `ログイン/新規登録` or the visible ASOBI STORE login entry.
2. On the ASOBI STORE login page, click `バンダイナムコIDでログイン`.
3. If a Bandai Namco ID account chooser or continuation screen appears and it does not require entering credentials, OTP, CAPTCHA, profile data, payment data, or account-setting changes, choose/continue the already-signed-in Bandai Namco ID.
4. After redirect, verify ASOBI STORE shows a named logged-in state such as `こんにちは ...様`, My Page, or logout.

Stop and ask the user only if the existing-session recovery cannot continue without credentials, OTP, CAPTCHA, account registration, profile/address input, account-link setup, a different-user warning, or account confirmation that affects account state. Never add items to cart, buy products, redeem purchase benefits, open payment flows, change account settings, or navigate purchase-category challenges for this skill.

## Verification And Report

Before finishing, re-open `/vote` and check that no in-scope daily card still shows `投票券を受け取れます` or an enabled `受け取る`. Optionally re-open `/vote/mission` to confirm no eligible daily `チャレンジ` remains. Report concisely:

- daily rewards collected, with ticket counts if visible from toasts
- daily rewards already collected or unavailable
- any skipped non-daily categories encountered
- whether login was required or blocked the run
