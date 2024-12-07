/*const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  publicPath:"/",
  transpileDependencies: true,
  outputDir: "build",
  indexPath: "index.html"
})*/

const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  outputDir: "dist",
  assetsDir: "static",
  indexPath: "index.html"
})
