const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  publicPath:"/static/",
  transpileDependencies: true,
  outputDir: "../static",
  indexPath: "index.html"
})
