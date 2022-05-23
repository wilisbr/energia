const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  publicPath:"/",
  transpileDependencies: true,
  outputDir: "build",
  indexPath: "index.html"
})
