import { HTTP } from '@/utils'
import * as types from './mutation-types'

export const getCSRFToken = ({ commit }) => {
  HTTP
    .get(`csrftoken/`)
    .then((response) => {
      commit(types.SET_CSRFTOKEN, response.data.csrftoken)
    }, (error) => {
      console.log(error)
    })
}
