import { useEffect, useMemo, useRef, useState } from 'react'
import type { Lang } from '../data'

type Props = { lang: Lang }

const stages = [
  { at: 0, zh: '輸入等式', en: 'equations in' },
  { at: 22, zh: '結構正規化', en: 'normalize' },
  { at: 46, zh: '有界搜尋', en: 'bounded search' },
  { at: 70, zh: '證書候選', en: 'candidate' },
  { at: 90, zh: 'Lean 裁判', en: 'Lean judge' },
  { at: 99, zh: '可計分事實', en: 'scored fact' },
]

export default function ProofPress({ lang }: Props) {
  const [pressure, setPressure] = useState(16)
  const [mode, setMode] = useState<'true' | 'false'>('true')
  const [running, setRunning] = useState(false)
  const frame = useRef<number | null>(null)

  const stage = useMemo(() => {
    let current = stages[0]
    for (const candidate of stages) if (pressure >= candidate.at) current = candidate
    return current
  }, [pressure])

  useEffect(() => () => {
    if (frame.current) cancelAnimationFrame(frame.current)
  }, [])

  const runPress = () => {
    if (frame.current) cancelAnimationFrame(frame.current)
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches
    if (reduceMotion) {
      setPressure(100)
      return
    }
    setRunning(true)
    const start = performance.now()
    const duration = 3100
    const tick = (now: number) => {
      const raw = Math.min(1, (now - start) / duration)
      const eased = raw < 0.72
        ? 0.72 * (1 - Math.pow(1 - raw / 0.72, 3))
        : 0.72 + 0.28 * (1 - Math.pow(1 - (raw - 0.72) / 0.28, 3))
      setPressure(Math.round(Math.min(1, eased) * 100))
      if (raw < 1) frame.current = requestAnimationFrame(tick)
      else setRunning(false)
    }
    setPressure(0)
    frame.current = requestAnimationFrame(tick)
  }

  const copy = {
    true: lang === 'zh' ? '證明蘊含' : 'prove implication',
    false: lang === 'zh' ? '構造反模型' : 'build countermodel',
    instruction: lang === 'zh' ? '拖動壓力桿，或啟動一次完整壓印' : 'Drag the pressure lever, or run one complete impression',
    press: lang === 'zh' ? '啟動壓印' : 'Run the press',
    running: lang === 'zh' ? '正在壓印…' : 'Pressing…',
    only: lang === 'zh' ? '只有透過 Lean 的證書才會留下紅印。' : 'Only a Lean-accepted certificate receives the red seal.',
    rejected: lang === 'zh' ? '未驗證的猜測在這裡被擋下' : 'unverified guesses stop here',
    accepted: lang === 'zh' ? 'ACCEPTED · 可重放' : 'ACCEPTED · REPLAYABLE',
  }

  const tokenX = 96 + pressure * 4.35
  const searchY = mode === 'true' ? 160 : 242
  const sealScale = pressure >= 99 ? 1 : 0

  return (
    <div className="press-shell" data-complete={pressure >= 99}>
      <div className="press-toolbar" aria-label={lang === 'zh' ? '證明路線控制' : 'Proof route controls'}>
        <div className="route-switch" role="group" aria-label={lang === 'zh' ? '選擇證書型別' : 'Choose certificate type'}>
          <button type="button" className={mode === 'true' ? 'is-active' : ''} onClick={() => { setMode('true'); setPressure(16) }} aria-pressed={mode === 'true'}>
            TRUE <span>{copy.true}</span>
          </button>
          <button type="button" className={mode === 'false' ? 'is-active' : ''} onClick={() => { setMode('false'); setPressure(16) }} aria-pressed={mode === 'false'}>
            FALSE <span>{copy.false}</span>
          </button>
        </div>
        <div className="press-stage" aria-live="polite">
          <span>{String(stages.indexOf(stage) + 1).padStart(2, '0')} / 06</span>
          <strong>{lang === 'zh' ? stage.zh : stage.en}</strong>
        </div>
      </div>

      <div className="press-canvas" aria-hidden="true">
        <svg viewBox="0 0 650 360" role="img">
          <title>{lang === 'zh' ? '從輸入等式到 Lean 驗證證書的互動壓力機' : 'Interactive press from equations to a Lean-verified certificate'}</title>
          <defs>
            <filter id="rough"><feTurbulence baseFrequency=".025" numOctaves="2" seed="4" result="noise"/><feDisplacementMap in="SourceGraphic" in2="noise" scale="1.2"/></filter>
            <pattern id="hatch" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="8" stroke="currentColor" strokeWidth="1"/></pattern>
          </defs>

          <path className="press-rail" d={`M96 200 C180 200 185 ${searchY} 248 ${searchY} S330 200 382 200 S470 200 535 200`} />
          <path className="press-rail ghost" d="M96 242 C180 242 190 160 248 160" />
          <g className="equation-input" transform="translate(20 122)">
            <rect width="110" height="156" rx="2" />
            <text x="14" y="31" className="svg-kicker">EQUATION 01</text>
            <text x="14" y="65" className="svg-equation">x(yz)</text>
            <text x="14" y="88" className="svg-equation">= (xy)z</text>
            <line x1="14" y1="106" x2="94" y2="106" />
            <text x="14" y="130" className="svg-kicker">EQUATION 02</text>
          </g>

          <g className={`search-drum mode-${mode}`} transform="translate(248 201)">
            <circle r="62" />
            <circle r="45" />
            <path d="M-45 0H45M0-45V45M-32-32L32 32M32-32L-32 32" />
            <text textAnchor="middle" y="4">{mode === 'true' ? 'PROOF DAG' : 'FIN n'}</text>
          </g>

          <g className="judge-frame" transform="translate(390 80)">
            <path d="M0 0H138V212H0z" />
            <path d="M18 0V212M120 0V212M18 35H120" />
            <rect className="judge-block" x="35" y={56 + (100 - pressure) * .55} width="68" height="24" rx="2" />
            <text x="69" y="24" textAnchor="middle">LEAN 4.33.1</text>
            <text x="69" y="190" textAnchor="middle" className="svg-kicker">DETERMINISTIC JUDGE</text>
          </g>

          <g className="certificate-token" style={{ transform: `translate(${tokenX}px, ${searchY}px)` }}>
            <rect x="-25" y="-18" width="50" height="36" rx="2" />
            <path d="M-15-7H12M-15 0H16M-15 7H7" />
          </g>

          <g className="reject-arm" style={{ opacity: pressure >= 72 && pressure < 90 ? 1 : .18 }} transform="translate(367 262)">
            <path d="M0 0 28 35" />
            <text x="34" y="42">{copy.rejected}</text>
          </g>

          <g className="accepted-sheet" transform="translate(548 112)">
            <rect width="84" height="176" />
            <path d="M15 28H68M15 44H58M15 60H65M15 76H52" />
            <g className="seal" style={{ transform: `translate(42px, 122px) scale(${sealScale})` }}>
              <circle r="29" />
              <path d="m-13 0 9 9 18-22" />
            </g>
          </g>

          <text className="accepted-caption" x="590" y="318" textAnchor="middle" style={{ opacity: pressure >= 99 ? 1 : 0 }}>{copy.accepted}</text>
        </svg>
        <div className="pressure-readout"><span>{String(pressure).padStart(3, '0')}</span><small>proof pressure</small></div>
      </div>

      <div className="press-controls">
        <label>
          <span>{copy.instruction}</span>
          <input type="range" min="0" max="100" value={pressure} onChange={(event) => setPressure(Number(event.target.value))} aria-valuetext={lang === 'zh' ? stage.zh : stage.en} />
        </label>
        <button type="button" className="press-button" onClick={runPress} disabled={running}>
          <span>{running ? copy.running : copy.press}</span>
          <i aria-hidden="true">↘</i>
        </button>
      </div>
      <p className="press-rule">{copy.only}</p>
    </div>
  )
}
