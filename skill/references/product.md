# How Toで使う最新機能と根拠

確認日: 2026-11-18。ユーザーが指定した完成版 `/Users/hirotomo.ishii/atlier-base-v1/products/yarikuri` を参照する。
以下のコードパスは同製品フォルダを起点とする。製品ファイルは今回変更していない。

## 無料提供と広告の方針

2026-11-18のユーザーの最新指示を優先する。**無料提供を広告収益で支える方針**。
プロフィール・記事・告知で「広告なし」「無広告」を訴求しない。
旧製品資料にある広告を搭載しない記述は、今回の発信方針の根拠として使わない。
広告の掲載開始時期や形式は、この指示だけで決定済み・実装済みと扱わない。

## 現行の機能

| 機能 | 記事で説明できること | 確認した正本 |
|---|---|---|
| 日別残高 | 登録した入出金から日々の残高を計算。カレンダーとレポートで途中の減り方を見る | `apps/mobile/src/lib/balance.ts`、`src/features/report/ReportMonthView.tsx`（後者もapps/mobile配下） |
| 現在残高の更新 | 設定の「現在の残高を更新」で計算の起点を合わせる。過去の記録自体は変えない | `apps/mobile/src/features/settings/BalanceEditView.tsx` |
| 固定費・固定収入 | 定期的な出入りを登録。設定トップの導線名は「固定費・固定収入の設定」 | `apps/mobile/src/features/settings/SettingsHomeView.tsx`、`src/lib/recurring.ts`（後者もapps/mobile配下） |
| カード | 締め日、支払月、支払日から引落日を計算。支払月は当月・翌月。締め日超過で締め月が1か月先へ進む | `apps/mobile/src/lib/card.ts` の `closeMonth`、`payDateFor`、`debitDateOf` |
| カード利用入力 | 利用日に記録し、「クレジットカードで支払う」をオンにしてカードを選ぶ | `apps/mobile/src/features/input/InputFormView.tsx` |
| 予算の消化 | 単発支出に加え、対象月のカテゴリ付き固定支出を含む。カテゴリなし固定費は特定カテゴリの消化には入らない | `apps/mobile/src/lib/budget.ts` の `budgetUsedByCat` |
| 予算の引継ぎ | 設定した月以降へ予算を引き継ぐ | `apps/mobile/src/lib/budget.ts` の `budgetsFor` |
| 予算を使った場合 | 未使用予算を明日以降の日付へ日割り。支払い方法の割合とカード引落日を反映。未来日付の登録済み支出も残額から差し引く | `apps/mobile/src/lib/budgetSimulation.ts` |
| レポートの比較 | 「登録分を反映」と「予算を使った場合」を表示。後者は設定した予算を使う想定で、使える額の保証ではない | `apps/mobile/src/features/report/ReportMonthView.tsx` |
| 無料範囲 | 未来24か月、予算管理・予算反映残高を利用可能。カード無制限、全機能無料 | `apps/mobile/src/lib/plan.ts`、製品 `AGENTS.md`、`docs/sprints/sprint-69.md` |
| オフライン | 保存済みのカレンダー・レポート・現在残高を閲覧。すべての操作や最新値の取得ができるとは説明しない | `apps/mobile/src/data/useCachedQuery.ts` |

## 公開版と次版

開発記録 `docs/development/status.md` では、2026-11-13にversion 1.0の日本公開を確認済み。
2026-11-18の最新開発記録では1.0.1／Build 17はApp Reviewの審査待ち。一般公開済みとは扱わない。

最新コードでは「繰り返し設定」で1〜12か月周期、開始月・終了月を指定できる。
周期設定の操作記事は1.0.1の公開確認後に出す。初回3記事はこの新しい操作に依存しない。
古い掲載文や仕様書には過去の制限や古い予算消化説明もあるため、現行コードと最新決定を照合する。

## 説明の範囲

- 手入力中心。金融機関との連携、明細自動取得、OCR、複数口座の個別管理は案内しない。
- 「残高が減る日を画面で確認できる」と説明する。自動通知や自動的な安全額判定を案内しない。
- カードは登録設定に基づく予測。銀行休業日の自動補正や売上確定明細との自動照合を案内しない。
- 分割払いやリボ払いの返済シミュレーターとして説明しない。
- 予算の日割りは仮定。大きな買い物が集中する実際の日付を保証しない。
- 現在残高を合わせても、未登録の将来予定や過去のカテゴリ集計まで修復されたとは説明しない。
- 家計の資金繰りを扱う。事業用の請求書・売掛金管理・会計ソフトとして紹介しない。
- 「過去は記録しない」「12か月先まで」は現行説明に使わない。

## アカウントと案内先

note ID: `yarikuri_app`。既存プロフィールの記録を引き継ぎ、Chromeで旧表示名・旧小説プロフィールとログイン状態を再確認した。最新の反映状態は `NEXT-STEPS.md` を参照。

- note: https://note.com/yarikuri_app
- App Store: https://apps.apple.com/jp/app/id6817269400
- 製品サイト: https://yarikuri.atelierbase.app/

公開URLは製品の開発記録による。今回の原稿作成でApp Storeの現況をライブ確認したとは扱わない。
