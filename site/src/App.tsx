import { useEffect, useMemo, useRef, useState } from 'react'
import ProofPress from './components/ProofPress'
import HypothesisRiver from './components/HypothesisRiver'
import { artifacts, methods, type Lang } from './data'

const repoUrl = 'https://github.com/f0909172434/sair-stage2-proof-press'
const officialUrl = 'https://competition.sair.foundation/competitions/mathematics-distillation-challenge-equational-theories-stage2/overview'

const t = {
  zh: {
    nav: ['壓力機', '結果', '方法', '研究河流', '論文'],
    eyebrow: 'SAIR 數學蒸餾挑戰賽 · 等式理論 Stage 2',
    heroA: '把猜想', heroB: '壓成證明。',
    heroBody: '七個確定性 checkpoint、六十三個受治理假設、四份正式提交。整段研究只承認一種貨幣：能被 Lean 重放的證書。',
    explore: '啟動證明壓力機', source: '檢視公開原始碼',
    status: '官方狀態：EVALUATING', submitted: '4 份提交已讀回',
    pressKicker: '核心體驗裝置 · Proof Press',
    pressTitle: '一條結果，必須穿過四道壓力。',
    pressBody: '結構選擇搜尋路線；搜尋只能提出候選；候選必須經過確定性 Lean judge；只有 accepted 才能進入結果表。拖動壓力桿，親自走完這條因果鏈。',
    resultKicker: '公開輸入結果 · 不是私人排行榜',
    resultTitle: '強結果，窄宣告。',
    resultBody: '四份最終 artifact 在 1,669 個已公開 Normal／Hard 輸入上全部透過。這個數字證明相容性與覆蓋，不代表隱藏分佈表現。',
    artifacts: '四份凍結提交',
    order5: 'Order-5', model: '模型槽位', bytes: '大小', hash: 'SHA-256', publicRows: '公開 1,669',
    methodKicker: '確定性優先 · 七道證書路線',
    methodTitle: '模型可以提議，不能裁決。',
    methodBody: '相同的判斷原則貫穿每一層：先做便宜、結構化、可重放的工作；只在剩餘問題上增加搜尋；最終把所有信念交給 Lean。',
    riverKicker: 'H1—H63 · 研究不是勝利遊行',
    riverTitle: '失敗、阻斷與無結果，也要保留原名。',
    riverBody: '點選任一編號檢視它真正回答了什麼。這裡刻意不把基礎設施錯誤包裝成科學負結果，也不把相容性測試包裝成新數學能力。',
    claimsKicker: '宣告語法 · Claim grammar',
    claimsTitle: '證據先決定句子的動詞。',
    claimsBody: '「透過」「失敗」「阻斷」「已提交」互不等價。我們把它們分開，是為了讓讀者能從頁面一路追溯到證書、評估器與凍結身分。',
    publicKicker: '開放研究 · 官方 Contributor Network',
    publicTitle: '公開不是結案，而是讓下一條證明有出處。',
    publicBody: '官方 Contributor Network 在比賽與評測期間持續公開 Stage 2 solver，允許研究者引用並繼續建構。本專案因此公開經過安全篩選的研究快照，同時把私人評測結果保持為空。',
    paperKicker: '六頁研究論文 · 可重現附件',
    paperTitle: '從 162/200 到四份最終 solver。',
    paperBody: '論文記錄確定性 solver 的演進、H19 與 H22、成本、失效的測量基底，以及為什麼 1,669/1,669 仍不能寫成排行榜成績。',
    readPaper: '下載雙語研究資料', cite: '引用本專案',
    footer: '以 Lean 證書為事實邊界。',
    inspect: '檢視證據底板', close: '關閉',
    evidenceLabel: '當前證據狀態',
    evidenceStages: ['猜想', '候選', 'Lean 裁決', '可宣告事實'],
  },
  en: {
    nav: ['Press', 'Results', 'Method', 'Research river', 'Paper'],
    eyebrow: 'SAIR Mathematics Distillation Challenge · Equational Theories Stage 2',
    heroA: 'Press conjectures', heroB: 'into proof.',
    heroBody: 'Seven deterministic checkpoints, sixty-three governed hypotheses, and four formal submissions. The record accepts one currency: certificates Lean can replay.',
    explore: 'Run the proof press', source: 'View public source',
    status: 'Official status: EVALUATING', submitted: '4 submissions read back',
    pressKicker: 'Core experience · Proof Press',
    pressTitle: 'A result must survive four kinds of pressure.',
    pressBody: 'Structure selects a route. Search may only propose. A deterministic Lean judge decides. Only accepted certificates enter the result table. Drag the lever to traverse that causal chain.',
    resultKicker: 'Released-input results · not a private leaderboard',
    resultTitle: 'Strong result. Narrow claim.',
    resultBody: 'All four final artifacts passed all 1,669 released Normal/Hard inputs. That establishes compatibility and coverage—not hidden-distribution performance.',
    artifacts: 'Four frozen submissions',
    order5: 'Order-5', model: 'Model slot', bytes: 'Bytes', hash: 'SHA-256', publicRows: 'Released 1,669',
    methodKicker: 'Deterministic first · seven certificate lanes',
    methodTitle: 'A model may propose. It cannot decide.',
    methodBody: 'One judgment runs through every layer: do cheap, structural, replayable work first; add search only for residuals; submit every belief to Lean.',
    riverKicker: 'H1—H63 · research is not a victory parade',
    riverTitle: 'Failures, blocks, and non-results keep their names.',
    riverBody: 'Select any index to see what it actually answered. Infrastructure defects are not scientific negatives; compatibility checks are not new mathematical capability.',
    claimsKicker: 'Claim grammar',
    claimsTitle: 'Evidence chooses the verb.',
    claimsBody: 'Passed, failed, blocked, and submitted are not synonyms. Separating them lets a reader trace every sentence back to a certificate, evaluator, and frozen identity.',
    publicKicker: 'Open research · official Contributor Network',
    publicTitle: 'Publication is not closure. It gives the next proof provenance.',
    publicBody: 'The official Contributor Network published Stage 2 solvers throughout the competition and evaluation, inviting citation and reuse. This project therefore releases a security-filtered research snapshot while leaving private results blank.',
    paperKicker: 'Six-page paper · reproducibility appendix',
    paperTitle: 'From 162/200 to four final solvers.',
    paperBody: 'The paper records the deterministic lineage, H19 and H22, cost, failed measurement substrates, and why 1,669/1,669 is still not a leaderboard score.',
    readPaper: 'Download research paper', cite: 'Cite this project',
    footer: 'Lean certificates are the fact boundary.',
    inspect: 'Inspect evidence plate', close: 'Close',
    evidenceLabel: 'Current evidence state',
    evidenceStages: ['Conjecture', 'Candidate', 'Lean judge', 'Claimable fact'],
  },
}

const navIds = ['press', 'results', 'method', 'river', 'paper']

const chapterEvidenceStage: Record<string, number> = {
  hero: 0,
  press: 1,
  results: 3,
  method: 3,
  river: 3,
  claims: 3,
  public: 3,
  paper: 3,
}

const evidenceTargets = ['top', 'press', 'method', 'results']

function App() {
  const [lang, setLang] = useState<Lang>('zh')
  const [activeMethod, setActiveMethod] = useState(4)
  const [ledgerOpen, setLedgerOpen] = useState(false)
  const [chapter, setChapter] = useState('hero')
  const ledgerTriggerRef = useRef<HTMLButtonElement>(null)
  const ledgerCloseRef = useRef<HTMLButtonElement>(null)
  const copy = t[lang]
  const base = import.meta.env.BASE_URL

  useEffect(() => {
    document.documentElement.lang = lang === 'zh' ? 'zh-Hant' : 'en'
  }, [lang])

  useEffect(() => {
    const update = () => {
      const max = document.documentElement.scrollHeight - window.innerHeight
      document.documentElement.style.setProperty('--scroll-progress', String(max > 0 ? window.scrollY / max : 0))
    }
    update()
    window.addEventListener('scroll', update, { passive: true })
    return () => window.removeEventListener('scroll', update)
  }, [])

  useEffect(() => {
    const background = document.querySelectorAll<HTMLElement>('.masthead, .evidence-rail, main, footer')
    background.forEach((element) => { element.inert = ledgerOpen })
    if (ledgerOpen) requestAnimationFrame(() => ledgerCloseRef.current?.focus())
    return () => background.forEach((element) => { element.inert = false })
  }, [ledgerOpen])

  const closeLedger = () => {
    setLedgerOpen(false)
    requestAnimationFrame(() => ledgerTriggerRef.current?.focus())
  }

  useEffect(() => {
    const observer = new IntersectionObserver((entries) => {
      const visible = entries.filter((entry) => entry.isIntersecting).sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0]
      if (visible) setChapter((visible.target as HTMLElement).dataset.chapter ?? 'hero')
    }, { threshold: [0.25, 0.55], rootMargin: '-15% 0px -25%' })
    document.querySelectorAll<HTMLElement>('[data-chapter]').forEach((element) => observer.observe(element))
    return () => observer.disconnect()
  }, [])

  useEffect(() => {
    const onKey = (event: KeyboardEvent) => {
      if (event.key.toLowerCase() === 'g' && !event.metaKey && !event.ctrlKey && !(event.target instanceof HTMLInputElement)) setLedgerOpen((value) => !value)
      if (event.key === 'Escape') {
        setLedgerOpen(false)
        requestAnimationFrame(() => ledgerTriggerRef.current?.focus())
      }
    }
    window.addEventListener('keydown', onKey)
    return () => window.removeEventListener('keydown', onKey)
  }, [])

  const active = methods[activeMethod]
  const artifactRows = useMemo(() => artifacts, [])
  const evidenceStage = chapterEvidenceStage[chapter] ?? 0

  return (
    <div className="site" data-chapter={chapter}>
      <div className="scroll-rule" aria-hidden="true"><i /></div>
      <header className="masthead">
        <a href="#top" className="wordmark" aria-label="Proof Press home">
          <span className="mark"><i /><i /></span>
          <span>PROOF<br />PRESS</span>
        </a>
        <nav aria-label={lang === 'zh' ? '主要導航' : 'Main navigation'}>
          {copy.nav.map((label, index) => <a key={navIds[index]} href={`#${navIds[index]}`}>{label}</a>)}
        </nav>
        <div className="header-tools">
          <button ref={ledgerTriggerRef} type="button" className="ledger-trigger" onClick={() => setLedgerOpen(true)} title={`${copy.inspect} · G`}>
            <span aria-hidden="true">⌁</span><span className="sr-only">{copy.inspect}</span>
          </button>
          <button type="button" className="lang-toggle" onClick={() => setLang(lang === 'zh' ? 'en' : 'zh')}>
            <span className={lang === 'zh' ? 'active' : ''}>中</span><i /><span className={lang === 'en' ? 'active' : ''}>EN</span>
            <span className="sr-only">{lang === 'zh' ? 'Switch to English' : '切換至中文'}</span>
          </button>
        </div>
      </header>

      <aside className="evidence-rail" aria-label={copy.evidenceLabel} style={{ '--evidence-stage': evidenceStage } as React.CSSProperties}>
        <div className="evidence-rail-label"><span>{copy.evidenceLabel}</span><b>0{evidenceStage + 1}/04</b></div>
        <ol>
          {copy.evidenceStages.map((label, index) => (
            <li key={label} className={index === evidenceStage ? 'is-current' : index < evidenceStage ? 'is-passed' : ''}>
              <a href={`#${evidenceTargets[index]}`} aria-current={index === evidenceStage ? 'step' : undefined}>
                <i aria-hidden="true" />
                <span>{label}</span>
              </a>
            </li>
          ))}
        </ol>
      </aside>

      <main id="main">
        <section className="hero" id="top" data-chapter="hero">
          <div className="hero-copy">
            <p className="eyebrow">{copy.eyebrow}</p>
            <h1><span>{copy.heroA}</span><em>{copy.heroB}</em></h1>
            <p className="hero-deck">{copy.heroBody}</p>
            <div className="hero-actions">
              <a className="action primary" href="#press">{copy.explore}<span>↓</span></a>
              <a className="action text" href={repoUrl}>{copy.source}<span>↗</span></a>
            </div>
          </div>
          <div className="hero-plate" aria-hidden="true">
            <div className="plate-number">63</div>
            <svg viewBox="0 0 410 520">
              <path className="plate-orbit" d="M70 110C310 25 365 175 256 242S52 285 102 418s246 70 245-36" />
              <path className="plate-proof" d="m63 164 66-40 53 48 79-90 84 70-48 100 56 79-92 70-92-49-81 67-31-112 66-56z" />
              <circle cx="256" cy="242" r="46" />
              <path d="m233 241 17 18 34-44" />
            </svg>
            <div className="plate-label">GOVERNED<br />HYPOTHESES</div>
          </div>
          <div className="hero-status">
            <span><i className="pulse" />{copy.status}</span>
            <span>{copy.submitted}</span>
            <span>Lean 4.33.1</span>
          </div>
        </section>

        <section className="chapter press-chapter" id="press" data-chapter="press">
          <div className="chapter-head">
            <p className="kicker">{copy.pressKicker}</p>
            <h2>{copy.pressTitle}</h2>
            <p>{copy.pressBody}</p>
          </div>
          <ProofPress lang={lang} />
        </section>

        <section className="chapter results-chapter" id="results" data-chapter="results">
          <div className="results-intro">
            <div>
              <p className="kicker">{copy.resultKicker}</p>
              <h2>{copy.resultTitle}</h2>
            </div>
            <p>{copy.resultBody}</p>
          </div>
          <div className="result-ledger">
            <article className="result-primary"><span>RELEASED / VERIFIED</span><strong>1,669<small>/ 1,669</small></strong><p>{lang === 'zh' ? '四份 artifact · 零模型呼叫' : 'all four artifacts · zero model calls'}</p></article>
            <article><span>ORDER-5</span><strong>198<small>→ 200</small></strong><p>{lang === 'zh' ? 'Safe → Aggressive' : 'Safe → Aggressive'}</p></article>
            <article><span>MARATHON</span><strong>−9.92<small>%</small></strong><p>{lang === 'zh' ? '公開批次 solver wall time' : 'released-batch solver wall time'}</p></article>
            <article><span>PROVIDER COST</span><strong>$0.918<small>012780</small></strong><p>{lang === 'zh' ? 'H20—H27 正成本紀錄總計' : 'positive-cost records, H20—H27'}</p></article>
          </div>

          <div className="artifact-section">
            <div className="section-label"><span>04</span><h3>{copy.artifacts}</h3></div>
            <div className="artifact-table" role="table" aria-label={copy.artifacts}>
              <div className="artifact-row artifact-head" role="row">
                <span role="columnheader">Track / Variant</span><span role="columnheader">{copy.model}</span><span role="columnheader">{copy.bytes}</span><span role="columnheader">{copy.hash}</span><span role="columnheader">{copy.publicRows}</span><span role="columnheader">{copy.order5}</span>
              </div>
              {artifactRows.map((item) => (
                <div className="artifact-row" role="row" key={item.id}>
                  <span role="cell"><b>{item.track}</b><em>{item.variant}</em></span><span role="cell">{item.model}</span><span role="cell">{item.bytes}</span><code role="cell">{item.hash}</code><strong role="cell">{item.publicResult}</strong><span role="cell">{item.order5}</span>
                </div>
              ))}
            </div>
          </div>
        </section>

        <section className="chapter method-chapter" id="method" data-chapter="method">
          <div className="method-intro">
            <p className="kicker">{copy.methodKicker}</p>
            <h2>{copy.methodTitle}</h2>
            <p>{copy.methodBody}</p>
          </div>
          <div className="method-machine">
            <div className="method-list" role="tablist" aria-label={lang === 'zh' ? '證書路線' : 'Certificate lanes'}>
              {methods.map((item, index) => (
                <button
                  type="button"
                  key={item.id}
                  id={`method-tab-${item.id}`}
                  role="tab"
                  tabIndex={activeMethod === index ? 0 : -1}
                  aria-selected={activeMethod === index}
                  aria-controls="method-detail"
                  className={activeMethod === index ? 'is-active' : ''}
                  onClick={() => setActiveMethod(index)}
                  onKeyDown={(event) => {
                    if (!['ArrowRight', 'ArrowDown', 'ArrowLeft', 'ArrowUp', 'Home', 'End'].includes(event.key)) return
                    event.preventDefault()
                    const next = event.key === 'Home' ? 0 : event.key === 'End' ? methods.length - 1 : (index + (event.key === 'ArrowRight' || event.key === 'ArrowDown' ? 1 : -1) + methods.length) % methods.length
                    setActiveMethod(next)
                    requestAnimationFrame(() => document.getElementById(`method-tab-${methods[next].id}`)?.focus())
                  }}
                >
                  <span>{item.mark}</span><b>{item.title[lang]}</b><i>↘</i>
                </button>
              ))}
            </div>
            <article id="method-detail" className="method-detail" role="tabpanel" aria-labelledby={`method-tab-${active.id}`}>
              <div className="method-glyph" data-method={active.id} aria-hidden="true">
                <span>{active.mark}</span><i /><i /><i />
              </div>
              <p>LANE {active.mark}</p>
              <h3>{active.title[lang]}</h3>
              <p>{active.body[lang]}</p>
              <div className="method-rule"><span>candidate</span><i>→</i><span>Lean</span><i>→</i><strong>fact</strong></div>
            </article>
          </div>
        </section>

        <section className="chapter river-chapter" id="river" data-chapter="river">
          <div className="river-intro">
            <p className="kicker">{copy.riverKicker}</p>
            <h2>{copy.riverTitle}</h2>
            <p>{copy.riverBody}</p>
          </div>
          <HypothesisRiver lang={lang} />
        </section>

        <section className="chapter claims-chapter" data-chapter="claims">
          <div className="claims-copy">
            <p className="kicker">{copy.claimsKicker}</p>
            <h2>{copy.claimsTitle}</h2>
            <p>{copy.claimsBody}</p>
          </div>
          <div className="claim-strips">
            {[
              ['RELEASED-PUBLIC VERIFIED', lang === 'zh' ? '在指定公開輸入與 evaluator 上 accepted' : 'accepted on named released inputs and evaluator'],
              ['SCIENTIFIC FAIL', lang === 'zh' ? '只否定預序號產生器制與門檻' : 'negative only for the preregistered mechanism and gate'],
              ['BLOCKED / INVALID', lang === 'zh' ? '沒有科學結論' : 'no scientific conclusion'],
              ['FORMAL READBACK', lang === 'zh' ? '證明提交發生，不證明評估成功' : 'proves submission, not evaluation success'],
            ].map(([title, body], index) => <div key={title} style={{ '--strip-index': index } as React.CSSProperties}><span>0{index + 1}</span><strong>{title}</strong><p>{body}</p></div>)}
          </div>
        </section>

        <section className="chapter public-chapter" data-chapter="public">
          <div className="public-stamp" aria-hidden="true"><span>OPEN</span><i>RESEARCH</i></div>
          <div>
            <p className="kicker">{copy.publicKicker}</p>
            <h2>{copy.publicTitle}</h2>
            <p>{copy.publicBody}</p>
            <div className="network-dates"><span>2026.05.11</span><i /><span>2026.09.01</span><b>{lang === 'zh' ? '官方平臺持續公開 solver' : 'solvers shared on the official platform'}</b></div>
          </div>
        </section>

        <section className="chapter paper-chapter" id="paper" data-chapter="paper">
          <div className="paper-cover" aria-hidden="true">
            <div className="paper-spine">SAIR · STAGE 2 · 2026</div>
            <div className="paper-title">LEAN-CERTIFIED<br />EQUATIONAL<br />REASONING</div>
            <div className="paper-seal">1669<br /><span>verified</span></div>
            <div className="paper-folio">01—06</div>
          </div>
          <div className="paper-copy">
            <p className="kicker">{copy.paperKicker}</p>
            <h2>{copy.paperTitle}</h2>
            <p>{copy.paperBody}</p>
            <div className="paper-actions">
              <a className="action primary" href={`${base}paper/sair_stage2_solver_research.pdf`}><span>{copy.readPaper}</span><i>↓ PDF</i></a>
              <a className="action text" href={`${repoUrl}#citation--引用`}><span>{copy.cite}</span><i>↗</i></a>
            </div>
            <dl>
              <div><dt>Evaluator</dt><dd>817a4653…66a</dd></div>
              <div><dt>Lean</dt><dd>4.33.1</dd></div>
              <div><dt>License</dt><dd>Apache-2.0</dd></div>
            </dl>
          </div>
        </section>
      </main>

      <footer>
        <div className="wordmark footer-mark"><span className="mark"><i /><i /></span><span>PROOF<br />PRESS</span></div>
        <p>{copy.footer}</p>
        <div><a href={officialUrl}>SAIR Stage 2 ↗</a><a href={repoUrl}>GitHub ↗</a><span>© 2026 f0909172434</span></div>
      </footer>

      {ledgerOpen && (
        <div className="ledger-overlay" role="dialog" aria-modal="true" aria-labelledby="ledger-title" onMouseDown={(event) => { if (event.target === event.currentTarget) closeLedger() }} onKeyDown={(event) => { if (event.key === 'Tab') { event.preventDefault(); ledgerCloseRef.current?.focus() } }}>
          <article>
            <button ref={ledgerCloseRef} type="button" onClick={closeLedger}>{copy.close} <span>ESC</span></button>
            <p>PLATE / 817A465 / 4.33.1</p>
            <h2 id="ledger-title">{copy.inspect}</h2>
            <div className="ledger-grid">
              <span>FINAL PACKET</span><strong>PASS</strong>
              <span>FOCUSED CONTRACTS</span><strong>9 / 9</strong>
              <span>SOLO SMOKE</span><strong>20 / 20 × 2</strong>
              <span>MARATHON SMOKE</span><strong>5 / 5 × 2</strong>
              <span>PRIVATE SCORE</span><strong>UNAVAILABLE</strong>
              <span>PROVIDER CALLS · FINAL PUBLIC</span><strong>0</strong>
            </div>
            <p className="ledger-note">{lang === 'zh' ? '按 G 可隨時開啟或收起這塊底板。這裡列的是稽核事實，不是排行榜結果。' : 'Press G to toggle this plate. These are audit facts, not leaderboard results.'}</p>
          </article>
        </div>
      )}
    </div>
  )
}

export default App
