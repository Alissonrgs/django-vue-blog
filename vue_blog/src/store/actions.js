import axios from 'axios'
import * as types from './mutation-types'

export const getCSRFToken = ({ commit }) => {
  axios
    .get('http://localhost:8000/csrftoken/')
    .then((response) => {
      commit(types.SET_CSRFTOKEN, response.data.csrftoken)
    }, (error) => {
      console.log(error)
    })
}
