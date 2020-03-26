<template>
  <div id="main">
    <head>
      <link
        href="https://fonts.googleapis.com/css?family=Roboto&display=swap"
        rel="stylesheet"
      />
      <link
        rel="stylesheet"
        href="https://use.fontawesome.com/releases/v5.7.0/css/all.css"
        integrity="sha384-lZN37f5QGtY3VHgisS14W3ExzMWZxybE1SJSEsQp9S+oqd12jhcu+A56Ebc1zFSJ"
        crossorigin="anonymous"
      />
    </head>
    <div id="navbar">
      <h1 id="name" class="pa-2">Austen Cote</h1>
      <v-spacer></v-spacer>
      <v-btn id="button" to="/" rounded color="info">home</v-btn>
      <v-btn id="button" to="/about" rounded class="ma-1" color="info"
        >Contact</v-btn
      >
      <v-btn id="button" to="/projects" rounded color="info">Projects</v-btn>
    </div>

    <div id="pictureDiv">
      <div id="img1" class="">
        <img id="img" src="tetons.JPG" alt="Image 1" />
      </div>
      <div id="img2">
        <img id="img" src="little.jpg" alt="Image 2" />
      </div>
      <div id="img3" class="">
        <img id="img" src="smith.jpg" alt="Image 3" />
      </div>
    </div>
    <div id="middleBlock">
      <p>
        Hello! I'm Austen, a software developer based in Portland, OR. I love
        building things that provide people with enjoyable internet experiences.
      </p>
      <p>
        I am a Veteran that is striving to make a seamless transition from
        Marine to Software Developer.
      </p>
    </div>
    <h2 id="skillsTitle">
      <strong><em>Technical Skills</em></strong>
    </h2>
    <hr />
    <div id="skills">
      <div>
        <strong>Programming Languages:</strong>
        <div id="langTitle">
          <p class="text-left ml-5 pt-2">- JavaScript</p>
          <p class="text-left ml-5">- Python</p>
          <p class="text-left ml-5">- HTML5</p>
          <p class="text-left ml-5">- CSS3</p>
        </div>
      </div>
      <div>
        <strong>Libraries:</strong>
        <div id="langTitle">
          <p class="text-left pt-2">- Vue Cli</p>
          <p class="text-left">- Vuex</p>
          <p class="text-left">- Vue Router</p>
          <p class="text-left">- Django</p>
          <p class="text-left">- Django Rest Api</p>
          <p class="text-left">- Vuetify</p>
        </div>
      </div>
      <div>
        <strong>Misc:</strong>
        <div id="langTitle">
          <p class="text-left pt-2 pl-4">- Git</p>
          <p class="text-left pl-4">- Github</p>
          <p class="text-left pl-4 ">- SQLite3</p>
          <p class="text-left pl-4 ">- JWT Authorization</p>
          <p class="text-left pl-4 ">- Windows/Mac</p>
          <p class="text-left pl-4 ">- Data Visualization</p>
        </div>
      </div>
    </div>
    <div id="contactInfo">
      <h2><strong>Contact Information:</strong></h2>
      <h4 class="email">Email: coteausten@gmail.com</h4>
      <a
        id="externalLinks"
        href="https://www.linkedin.com/in/austen-cote-8ba6aa169/"
        ><i class="fab fa-linkedin fa-5x"></i
      ></a>
      <a id="externalLinks" href="https://github.com/aust10"
        ><i class="fab fa-github fa-5x"></i
      ></a>
    </div>
    <div id="bottomBar">
      <p>Produced by:<a href="#"> Austen Cote</a></p>
    </div>
  </div>
</template>

<script>
export default {
  components: {}
}
</script>
<style scoped>
main {
  background-color: #99564a;
  font-family: 'Roboto', sans-serif;
}
#name,
#button,
#middleBlock,
#skillsTitle,
strong,
#langTitle,
#contactInfo,
#bottomBar,
#skills {
  font-family: 'Roboto', sans-serif;
}
hr {
  margin-left: 30px;
  margin-right: 30px;
}
#navbar {
  display: flex;
  justify-content: space-between;
  margin: 5px;
  margin-right: 30px;
  margin-left: 30px;
}
#button {
  background-color: #546e7a;
  margin: 2px;
}
#externalLinks:hover {
  color: rgb(22, 183, 189);
}
#img {
  height: 280px;
  width: 300px;
  border-radius: 5px;
}
#pictureDiv {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-evenly;
  background-color: #546e7a;
  padding: 15px;
}
#middleBlock {
  text-align: center;
  margin-top: 20px;
}
#middleBlock p {
  margin: 20px;
}
#skillsTitle {
  margin-left: 50px;
}
#skills {
  display: flex;
  justify-content: space-evenly;
  margin: 20px 10px 0px 10px;
}
#langTitle {
  padding: 10px;
}
#langTitle p {
  padding-top: 5px;
  padding-bottom: 5px;
}
#contactInfo {
  margin: 20px;
  text-align: center;
}
#contactInfo h4 {
  margin-top: 10px;
  margin-bottom: 10px;
}
#bottomBar {
  margin-left: 10px;
}
#bottomBar,
p,
a {
  color: black;
}
@media (max-width: 425px) {
  #button {
    display: none;
  }
  #name {
    text-align: center;
  }
}
</style>
