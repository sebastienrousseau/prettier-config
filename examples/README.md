# `@sebastienrousseau/prettier-config` Examples Catalog

This directory provides runnable, standalone examples covering **100% of the functionalities and features** provided by `@sebastienrousseau/prettier-config`.

---

## Example Suite Overview

| File                           | Type      | Feature Coverage                       | Command                     |
| :----------------------------- | :-------- | :------------------------------------- | :-------------------------- |
| [`basic.js`](./basic.js)       | CommonJS  | Standard default configuration import  | `node examples/basic.js`    |
| [`advanced.js`](./advanced.js) | CommonJS  | Custom extension and rule overrides    | `node examples/advanced.js` |
| [`esm.mjs`](./esm.mjs)         | ES Module | Native ESM consumption via `import`    | `node examples/esm.mjs`     |
| [`features.js`](./features.js) | CommonJS  | **100% feature showcase & assertions** | `node examples/features.js` |

---

## 100% Feature Coverage Checklist

- [x] **Schema Validation**: Adheres to schemastore.org prettierrc specification
- [x] **2-Space Indentation**: Enforces clean 2-space soft tabs (`tabWidth: 2`, `useTabs: false`)
- [x] **Unix Line Endings**: Enforces consistent LF line feeds across operating systems
- [x] **Consistent Quotes & Semicolons**: Double quotes and explicit semicolons
- [x] **Trailing Commas**: Enforces multi-line trailing commas (`trailingComma: 'all'`)
- [x] **Dual Packaging**: Full interoperability across CommonJS (`.cjs`, `.js`) and ECMAScript Modules (`.mjs`).

---

## Running All Examples

You can run and validate the entire example suite with:

```bash
npm run examples
```
