<template>
  <div class="row">
    <div class="col-md-12">
      <b-breadcrumb :items="breadcrumb" />

      <p>Response: {{ data }}</p>

      <form @submit.prevent="signIn">
        <fieldset>
          <div class="form-group">
            <div class="row">
              <label class="col-md-4 control-label text-right">Username</label>
              <div class="col-md-4">
                <input v-model="username" class="form-control" type="text">
              </div>
            </div>
          </div>
          <div class="form-group">
            <div class="row">
              <label class="col-md-4 control-label text-right">Password</label>
              <div class="col-md-4">
                <input v-model="password" class="form-control" type="password">
              </div>
            </div>
          </div>
          <div class="form-actions col-md-12 text-center">
            <button @keyup.enter="submit" class="btn btn-primary">Login</button>
          </div>
        </fieldset>
      </form>

      <ul v-if="errors && errors.length">
        <li v-for="error of errors">{{ error.message }}</li>
        <li>{{ errors }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
import { HTTP } from '@/utils'

export default {
  name: 'login',
  data: () => ({
    breadcrumb: [
      { text: '<i class="fa fa-sign-in" aria-hidden="true"></i> Login', link: '/' }
    ],
    username: '',
    password: '',
    data: [],
    errors: []
  }),
  methods: {
    signIn () {
      HTTP({
        method: 'POST',
        url: `o/token/`,
        headers: {
          'X-CSRFToken': this.$store.state.csrftoken
        },
        data: {
          grant_type: 'password',
          username: this.username,
          password: this.password,
          scope: 'read',
          client_id: 'gFwqIENKSJtFAKumGVE9nDO9qyFWhVOFGnaCfPG0',
          client_secret: 'kfYR7Ow7Os1ybXNu9eTeky0E5WHFKlGUlQEstnuQLNjOliNMMosJuKdZc0Y2qhgF0XWW6SwG5b0xAyOOFoeIUSFpEbSAJjJ9W4jfMQFsrNVBAGCghiUNlJnvcbQP2gCV'
        }
      })
      .then(response => {
        console.log(response)
        console.log(response.headers)
        this.data = response.data
      }).catch(errors => {
        this.errors = errors
      })
    }
  }
}
</script>
