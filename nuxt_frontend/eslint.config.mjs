// @ts-check
import withNuxt from "./.nuxt/eslint.config.mjs";
import prettierPlugin from "eslint-plugin-prettier";

export default withNuxt([
  // ...other configs,
  {
    plugins: {
      prettier: prettierPlugin,
    },
    rules: {
      // @ts-ignore
      ...prettierPlugin.configs.recommended.rules,
    },
  },
]);
