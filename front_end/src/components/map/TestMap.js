import React, { useEffect, useState } from 'react'
import useMap from './useBMap'

const TestMap = (props) => {
  const [BMap] = useMap('map')
  const [bMap, setMap] = useState(null)
  useEffect(() => {
    if (BMap) {
      const map = new BMap.Map('bMap')
      map.centerAndZoom('北京', 15)
      map.enableScrollWheelZoom()
      setMap(map)
    }
  }, [BMap])
  return (
            <div>
              <div id='bMap' style={{ width: 500, height: 500 }}></div>
              <button onClick={() => { bMap.centerAndZoom('广州', 15) }}>广州</button>
              <button onClick={() => { bMap.centerAndZoom('北京', 15) }}>北京</button>
              <button onClick={() => { bMap.centerAndZoom('上海', 15) }}>上海</button>
            </div>
  )
}

export default TestMap
