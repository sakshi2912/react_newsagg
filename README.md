# react_newsagg
News Aggregator using React JS and Django 

Create two apps with react as front-end and django as backend 

Packages to be installed in frontend :
 1. Babel : npm install @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev
 2. React : npm install react react-dom --save-dev
 3. Webpack : npm install webpack webpack-cli --save-dev

1.Configure the packages with : 
 a..babelrc
 b.webpack.config.js

2.Configuren package.json with these scripts :
"scripts": {
  "dev": "webpack --mode development ./src/index.js --output ./static/frontend/main.js",
  "build": "webpack --mode production ./src/index.js --output ./static/frontend/main.js"
}

3.Run " npm run dev" to save changes made to js files 
4.Run python manage.server to host the server 
