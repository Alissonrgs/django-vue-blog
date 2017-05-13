<template>
  <div class="row">
    <div class="col-md-12">
      <b-breadcrumb :items="breadcrumb" />

      http://bootsnipp.com/snippets/featured/comment-box

      <form @submit.prevent="postPost">
        <div class="form-inline">
          <label for="author">Author: </label>
          <select v-model="author" id="author">
            <option v-for="user of users" class="form-control" :value="user.pk">{{ user.username }}</option>
          </select>
        </div>

        <br />

        <div class="form-group">
          <textarea v-model="description" class="form-control" placeholder="Description"></textarea>
        </div>

        <div class="form-inline">
          <input class="form-control btn btn-primary" type="submit" value="Post">
        </div>
      </form>

      <br />

      <div v-for="post of posts" class="row">
        <b-card :header="getName(post.author)" class="col-md-12 text-center" :title="post.description" sub-title="" show-footer>
          <small slot="footer" class="text-muted">
              {{ post.posted | formatDate }}
          </small>
        </b-card>
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
import {HTTP} from '@/common'

export default {
  name: 'posts',
  data: () => ({
    breadcrumb: [
      { text: '<i class="fa fa-sign-in" aria-hidden="true"></i> Login', link: '/' },
      { text: '<i class="fa fa-comment-o" aria-hidden="true"></i> Posts', link: '/posts/' }
    ],
    pk: 0,
    author: 0,
    description: '',
    users: [],
    posts: [],
    errors: []
  }),
  methods: {
    checkPk: function (user) {
      return user['pk'] === this.pk
    },
    getName: function (pk) {
      this.pk = pk
      return this.users.find(this.checkPk).username
    },
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
    postPost: function () {
      HTTP
        .post(`posts/`, {
          author: this.author,
          description: this.description,
          status: true
        })
        .then(response => {
          console.log(response)
          this.posts = this.posts.concat(response.data)
          this.posts = this.sortedArray(this.posts, 'posted', true)
        })
        .catch(e => {
          this.errors.add(e)
        })
    }
  },
  mounted () {
    HTTP
      .get(`users`)
      .then(response => {
        this.users = response.data
        console.log(response)
      })
      .catch(e => {
        this.errors.push(e)
      })
    HTTP
      .get(`posts`)
      .then(response => {
        console.log(response)
        this.posts = response.data
      })
      .catch(e => {
        this.errors.push(e)
      })
  }
}
</script>
