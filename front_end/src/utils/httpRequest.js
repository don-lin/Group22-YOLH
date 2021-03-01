import axios from 'axios'

const serverConfig = {
    serverURL: 'https://www.kaiheila.cn',
    apiVersion: 1
}

export default class {

    constructor() {
        const config = {
            baseURL: `${serverConfig.serverURL}/api/v${serverConfig.apiVersion}`
        }
        this.requestor = axios.create(config)

    }

    async get(url, params = {}) {
        let result
        await this.requestor.get(url, { params })
            .then(response => result = response.data)
            .catch(response => { throw response })
        return result
    }

    async post(url, data = {}) {
        let result
        await this.requestor.post(url, data, { headers: { 'Content-type': 'application/json' } })
            .then(response => result = response.data)
            .catch(response => { throw response })
        return result
    }

}