import * as types from './mutation-types'

const mutations = {
  [types.SET_CSRFTOKEN] (state, csrftoken) {
    state.csrftoken = csrftoken
  }
}

export default mutations
