import { useMemo, useRef, useState } from 'react'
import { hypotheses, statusLabels, type HypothesisStatus, type Lang } from '../data'

type Props = { lang: Lang }
type Filter = 'all' | HypothesisStatus

const filterOrder: Filter[] = ['all', 'reused', 'pass', 'scientific-fail', 'source', 'blocked', 'no-successor']

export default function HypothesisRiver({ lang }: Props) {
  const [filter, setFilter] = useState<Filter>('all')
  const [selected, setSelected] = useState(19)
  const cells = useRef<Array<HTMLButtonElement | null>>([])
  const active = hypotheses.find((item) => item.id === selected) ?? hypotheses[18]
  const counts = useMemo(() => Object.fromEntries(filterOrder.map((key) => [key, key === 'all' ? hypotheses.length : hypotheses.filter((item) => item.status === key).length])), [])

  const label = (key: Filter) => {
    if (key === 'all') return lang === 'zh' ? '全部' : 'all'
    return statusLabels[key][lang]
  }

  return (
    <div className="river-shell">
      <div className="river-filters" role="toolbar" aria-label={lang === 'zh' ? '依結果篩選假設' : 'Filter hypotheses by outcome'}>
        {filterOrder.map((key) => (
          <button key={key} type="button" className={filter === key ? 'is-active' : ''} onClick={() => setFilter(key)} aria-pressed={filter === key}>
            <span>{label(key)}</span><b>{counts[key]}</b>
          </button>
        ))}
      </div>

      <div className="river-grid" aria-label={lang === 'zh' ? 'H1 至 H63 結果圖' : 'Outcome map for H1 through H63'}>
        {hypotheses.map((item) => {
          const dimmed = filter !== 'all' && item.status !== filter
          return (
            <button
              type="button"
              key={item.id}
              className={`river-cell status-${item.status} ${selected === item.id ? 'is-selected' : ''}`}
              data-dimmed={dimmed}
              ref={(element) => { cells.current[item.id - 1] = element }}
              tabIndex={selected === item.id ? 0 : -1}
              onClick={() => { setSelected(item.id); if (filter !== 'all' && item.status !== filter) setFilter('all') }}
              onKeyDown={(event) => {
                const columns = window.matchMedia('(max-width: 650px)').matches ? 5 : window.matchMedia('(max-width: 980px)').matches ? 7 : 9
                const delta = event.key === 'ArrowRight' ? 1 : event.key === 'ArrowLeft' ? -1 : event.key === 'ArrowDown' ? columns : event.key === 'ArrowUp' ? -columns : 0
                if (!delta) return
                event.preventDefault()
                const next = Math.min(hypotheses.length, Math.max(1, item.id + delta))
                setSelected(next)
                requestAnimationFrame(() => cells.current[next - 1]?.focus())
              }}
              aria-label={`H${item.id}: ${statusLabels[item.status][lang]}`}
              aria-pressed={selected === item.id}
            >
              <span>H{item.id}</span>
              <i aria-hidden="true" />
            </button>
          )
        })}
      </div>

      <article className={`river-detail status-${active.status}`} aria-live="polite">
        <div className="detail-index">H{String(active.id).padStart(2, '0')}</div>
        <div>
          <p>{statusLabels[active.status][lang]}</p>
          <h3>{active.copy[lang]}</h3>
        </div>
        <div className="detail-boundary">
          <span>{lang === 'zh' ? '宣告邊界' : 'claim boundary'}</span>
          <strong>{active.status === 'reused'
            ? (lang === 'zh' ? '支援最終方法譜系' : 'supports final method lineage')
            : active.status === 'scientific-fail'
              ? (lang === 'zh' ? '只否定預註冊範圍' : 'negative only within preregistered scope')
              : (lang === 'zh' ? '僅形成執行或治理結論' : 'supports an execution or governance conclusion only')}</strong>
        </div>
      </article>
    </div>
  )
}
