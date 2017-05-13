<template>
  <div class="container">
    <nav class="navbar navbar-default navbar-inverse">
      <div class="container-fluid">
        <div class="navbar-header">
          <a class="navbar-brand" href="#">SPA Blog - Django + Vue</a>
        </div>
        <div class="collapse navbar-collapse">
          <ul class="nav navbar-nav navbar-right">
            <li>
              <router-link :to="{ path: '/' }">
                <i class="fa fa-sign-in" aria-hidden="true"></i> Login
              </router-link>
            </li>
            <li>
              <router-link :to="{ path: '/users/' }">
                <i class="fa fa-users" aria-hidden="true"></i> Users
              </router-link>
            </li>
            <li>
              <router-link :to="{ path: '/posts/' }">
                <i class="fa fa-comment-o" aria-hidden="true"></i> Posts
              </router-link>
            </li>

            <li role="separator" class="divider"></li>

            <li>
              <a href=""><i class="fa fa-bars" aria-hidden="true"></i></a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <div class="row">
      <div class="col-md-12">
        <div class="panel panel-default">
          <div class="panel-heading text-center">
            <img src="./assets/logo.png">
          </div>
          <div class="panel-body">
            <router-view />
          </div>
          <div class="panel-footer">
            <br /><br /><br />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
