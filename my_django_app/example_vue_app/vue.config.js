const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const path = require('path');

module.exports = {
    publicPath: '/static/example_vue_app/', // Should be STATIC_URL + path/to/build
    outputDir: path.resolve(__dirname, '../static/example_vue_app/'), // Output to a directory in STATICFILES_DIRS
    filenameHashing: true, // Django will hash file names, not webpack
    runtimeCompiler: true, // See: https://vuejs.org/v2/guide/installation.html#Runtime-Compiler-vs-Runtime-only
    devServer: {
      devMiddleware: {
        // see https://github.com/webpack/webpack-dev-server/issues/2958
        writeToDisk: true,
      }
    },
    configureWebpack: {
        plugins: [
            new CleanWebpackPlugin(),
        ]
    }
};
