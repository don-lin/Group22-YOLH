import { useEffect, useState } from 'react'
const useBMap = (mapId) => {
  const [{ BMap, BMapLib }, setMap] = useState({})
  const BM = function (key) {
    return new Promise(function (resolve, reject) {
      const script = document.createElement('script')
      script.type = 'text/javascript'
      script.src = `http://api.map.baidu.com/api?v=2.0&ak=${key}&callback=init`
      document.head.appendChild(script)
      window.init = () => {
        resolve(window.BMap, window.BMapLib)
      }
    })
  }
  useEffect(() => {
    BM('PAZGg1jfimrTHCIAsoQc9zfsRbh').then((BMap, BMapLib) => {
      setMap({ BMap, BMapLib })
    })
  }, [])
  return [BMap, BMapLib]
}

export default useBMap
