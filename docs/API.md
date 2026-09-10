# `@sebastienrousseau/prettier-config` API Specification

Comprehensive schema, property definitions, and exported options reference for `@sebastienrousseau/prettier-config`.

---

## Description

Shareable Prettier configuration enforcing clean, standardized code formatting.

---

## Programmatic Entrypoints

| Specifier | Module Type | Target Runtime | Path |
| :--- | :--- | :--- | :--- |
| `.` (default) | Dual (CJS/ESM) | Node.js >= 18 | `index.cjs` / `index.mjs` |
| `@sebastienrousseau/prettier-config` | Dual (CJS/ESM) | Node.js >= 18 | `index.cjs` / `index.mjs` |
| `index.d.ts` | TypeScript | TypeScript >= 5.0 | Type declarations |

---

## Feature & Property Reference

### 1. Schema Validation

- **Description**: Adheres to schemastore.org prettierrc specification
- **Scope**: Production & Development
- **Status**: Stable & Active

### 2. 2-Space Indentation

- **Description**: Enforces clean 2-space soft tabs (`tabWidth: 2`, `useTabs: false`)
- **Scope**: Production & Development
- **Status**: Stable & Active

### 3. Unix Line Endings

- **Description**: Enforces consistent LF line feeds across operating systems
- **Scope**: Production & Development
- **Status**: Stable & Active

### 4. Consistent Quotes & Semicolons

- **Description**: Double quotes and explicit semicolons
- **Scope**: Production & Development
- **Status**: Stable & Active

### 5. Trailing Commas

- **Description**: Enforces multi-line trailing commas (`trailingComma: 'all'`)
- **Scope**: Production & Development
- **Status**: Stable & Active

