import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [
    vue({
      template: {
        compilerOptions: {
          // Ignore sdx-web-components from vue compiler
          isCustomElement: tag => tag.startsWith('sdx-'),
        },
      },
    }),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    proxy: {
      // Proxy all requests starting with '/api' to your Flask backend
      '/api/fetch_entities': {
        target: 'http://0.0.0.0:5000',
        changeOrigin: true,
      }
    }
  }
})