var path = require('path')
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')


module.exports = {
  entry: './frontend/js/main.js',

  output: {
      path: path.resolve('./frontend/bundles/'),
      filename: "[name]-[hash].js"
  },

  plugins: [
    new BundleTracker({filename: './webpack-stats.json'}),
  ],

  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader'
      },
      {
        test: /\.js$/,
        loader: 'babel-loader',
        exclude: /node_modules/
      }
    ]
  }
}