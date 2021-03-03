
import ChartJs from 'chart.js'
import PropTypes from 'prop-types'

import React, { useEffect, useRef, useCallback, useMemo } from 'react'

const Chart = ({ data, options, type, plugins, updateMode, height, width }) => {
  const chartInstance = useRef({
    update: () => { },
    destroy: () => { }
  })
  const id = useMemo(() => Math.random().toString(36).slice(-8), [])

  useEffect(() => {
    chartInstance.current.data = data
    chartInstance.current.options = options
    chartInstance.current.update(updateMode)
  }, [type, data, options])

  const ref = useCallback(
    (node) => {
      chartInstance.current.destroy()

      if (node) {
        chartInstance.current = new ChartJs(node, {
          type,
          data,
          options,
          plugins
        })
      }
    },
    []
  )

  return <canvas ref={ref} height={height} width={width} id={id} />
}

Chart.propTypes = {
  data: PropTypes.object,
  options: PropTypes.object,
  type: PropTypes.string,
  plugins: PropTypes.array,
  updateMode: PropTypes.any,
  height: PropTypes.string,
  width: PropTypes.string
}
export default Chart
