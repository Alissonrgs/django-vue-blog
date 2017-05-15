<template>
  <div class="row">
    <div class="col-md-12">
      <b-breadcrumb :items="breadcrumb" />

      <form @submit.prevent="register" class="form-horizontal">
        <fieldset>
          <div class="form-group">
            <div class="row">
              <label class="col-md-2 control-label text-right">Username</label>
              <div class="col-md-4">
                <input v-model="username" class="form-control" placeholder="kallos" type="text">
              </div>
            </div>
          </div>
          <div class="form-group">
            <div class="row">
              <label class="col-md-2 control-label text-right">Email address</label>
              <div class="col-md-4">
                <input v-model="email" class="form-control" placeholder="kallos@email.com" type="email">
              </div>
            </div>
          </div>
          <div class="form-group">
            <div class="row">
              <label class="col-md-2 control-label text-right">Password</label>
              <div class="col-md-4">
                <input v-model="password1" class="form-control" placeholder="@K4ll05" type="password">
              </div>
            </div>
          </div>
          <div class="form-group">
            <div class="row">
              <label class="col-md-2 control-label text-right">Password Confirm</label>
              <div class="col-md-4">
                <input v-model="password2" class="form-control" placeholder="@K4ll05" type="password">
              </div>
            </div>
          </div>
          <div class="form-actions col-md-6 text-right">
            <button @keyup.enter="submit" class="btn btn-primary" title="Make a POST request on the User Create resource">Register</button>
          </div>
        </fieldset>
      </form>
      <br /><br />
      <div class="row">
        <div class="col-md-6">
          <div class="form-inline">
            <label for="rows">Rows per page: </label>
            <select v-model="per_page" id="rows" class="form-control">
              <option>5</option>
              <option>10</option>
              <option>15</option>
            </select>
          </div>
        </div>
        <div class="col-sm-6">
          <div class="form-inline">
            <label for="search">Filter: </label>
            <input v-model="filter" class="form-control" placeholder="Search">
          </div>
        </div>
      </div>
      <br />
      <div class="row">
        <div class="col-md-12">
          <b-table striped hover :items="users" :fields="fields" :current-page="current_page" :per-page="per_page" :filter="filter">
            <template slot="is_staff" scope="field">
              {{ field.value ? 'Yes :)' : 'No :(' }}
            </template>
            <template slot="date_joined" scope="field">
              {{ field.value | formatDate }}
            </template>
          </b-table>
        </div>
      </div>
      <br />
      <div class="row">
        <div class="col-md-12">
          <b-pagination style="float: right;" size="md" :total-rows="this.users.length" :per-page="per_page" v-model="current_page" />
        </div>
      </div>

      <ul v-if="errors && errors.length">
        <li v-for="error of errors">
          {{ error.message }}
        </li>
        <li>{{ errors }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
import { HTTP } from '@/utils'

export default {
  name: 'users',
  data: () => ({
    breadcrumb: [
      { text: '<i class="fa fa-sign-in" aria-hidden="true"></i> Login', link: '/' },
      { text: '<i class="fa fa-users" aria-hidden="true"></i> Users', link: '/users/' }
    ],
    username: '',
    email: '',
    password1: '',
    password2: '',
    current_page: 1,
    per_page: 5,
    filter: null,
    fields: {
      username: { label: 'Username', sortable: true },
      email: { label: 'E-mail', sortable: true },
      is_staff: { label: 'Is Staff', sortable: true },
      date_joined: { label: 'Date Joined', sortable: true }
    },
    users: [],
    errors: []
  }),
  methods: {
    sortedArray: function (array, attr, inv) {
      function ord (a, b) {
        if (inv) {
          return a[attr] < b[attr] ? 1 : -1
        } else {
          return a[attr] > b[attr] ? 1 : -1
        }
      }
      return array.sort(ord)
    },
    register: function () {
      var password = ''
      if (this.password1 === this.password2) {
        password = this.password1
        HTTP({
          method: 'POST',
          url: 'users/create/',
          headers: {
            'X-CSRFToken': this.$store.state.csrftoken,
            'Authorization': 'Bearer 5UOoEWYbWuerT5IldBNKqdlSOfd5Ph'
          },
          data: {
            username: this.username,
            email: this.email,
            password: password
          }
        })
        .then(response => {
          console.log(response)
          this.users = this.users.concat(response.data)
          this.users = this.sortedArray(this.users, 'date_joined', true)
        })
        .catch(e => {
          this.errors.push(e)
        })
      } else {
        alert('There is a difference in passwords!')
      }
    }
  },
  mounted () {
    HTTP({
      method: 'GET',
      url: 'v1/users/',
      headers: {
        'Authorization': 'Bearer 5UOoEWYbWuerT5IldBNKqdlSOfd5Ph'
      }
    })
    .then(response => {
      this.users = response.data
      console.log(response)
      console.log(response.headers)
    })
    .catch(e => {
      this.errors.push(e)
    })
  }
}
</script>
