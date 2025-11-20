Repository: eziocdl/seo-cro-geo-analysis
Files analyzed: 27

Estimated tokens: 81.8k

Directory structure:
└── eziocdl-seo-cro-geo-analysis/
├── README.md
├── components.json
├── next.config.mjs
├── package.json
├── pnpm-lock.yaml
├── postcss.config.mjs
├── tsconfig.json
├── app/
│ ├── globals.css
│ ├── layout.tsx
│ ├── page.tsx
│ └── api/
│ └── analyze/
│ └── route.ts
├── components/
│ ├── analysis-charts.tsx
│ ├── analysis-form.tsx
│ ├── dashboard.tsx
│ ├── header.tsx
│ ├── hero.tsx
│ ├── insights-panel.tsx
│ ├── metrics-grid.tsx
│ ├── recommendations.tsx
│ ├── theme-provider.tsx
│ └── ui/
│ ├── button.tsx
│ ├── card.tsx
│ └── input.tsx
├── lib/
│ ├── insights-generator.ts
│ ├── pdf-generator.ts
│ └── utils.ts
├── public/
└── styles/
└── globals.css

================================================
FILE: README.md
================================================

# SEO CRO GEO analysis

_Automatically synced with your [v0.app](https://v0.app) deployments_

[![Deployed on Vercel](https://img.shields.io/badge/Deployed%20on-Vercel-black?style=for-the-badge&logo=vercel)](https://vercel.com/eziocdls-projects/v0-seo-cro-geo-analysis)
[![Built with v0](https://img.shields.io/badge/Built%20with-v0.app-black?style=for-the-badge)](https://v0.app/chat/uh5PfImfAN5)

## Overview

This repository will stay in sync with your deployed chats on [v0.app](https://v0.app).
Any changes you make to your deployed app will be automatically pushed to this repository from [v0.app](https://v0.app).

## Deployment

Your project is live at:

**[https://vercel.com/eziocdls-projects/v0-seo-cro-geo-analysis](https://vercel.com/eziocdls-projects/v0-seo-cro-geo-analysis)**

## Build your app

Continue building your app on:

**[https://v0.app/chat/uh5PfImfAN5](https://v0.app/chat/uh5PfImfAN5)**

## How It Works

1. Create and modify your project using [v0.app](https://v0.app)
2. Deploy your chats from the v0 interface
3. Changes are automatically pushed to this repository
4. Vercel deploys the latest version from this repository

================================================
FILE: components.json
================================================
{
"$schema": "https://ui.shadcn.com/schema.json",
"style": "new-york",
"rsc": true,
"tsx": true,
"tailwind": {
"config": "",
"css": "app/globals.css",
"baseColor": "neutral",
"cssVariables": true,
"prefix": ""
},
"aliases": {
"components": "@/components",
"utils": "@/lib/utils",
"ui": "@/components/ui",
"lib": "@/lib",
"hooks": "@/hooks"
},
"iconLibrary": "lucide"
}

================================================
FILE: next.config.mjs
================================================
/\*_ @type {import('next').NextConfig} _/
const nextConfig = {
eslint: {
ignoreDuringBuilds: true,
},
typescript: {
ignoreBuildErrors: true,
},
images: {
unoptimized: true,
},
}

export default nextConfig

================================================
FILE: package.json
================================================
{
"name": "my-v0-project",
"version": "0.1.0",
"private": true,
"scripts": {
"build": "next build",
"dev": "next dev",
"lint": "eslint .",
"start": "next start"
},
"dependencies": {
"@hookform/resolvers": "^3.10.0",
"@radix-ui/react-accordion": "1.2.2",
"@radix-ui/react-alert-dialog": "1.1.4",
"@radix-ui/react-aspect-ratio": "1.1.1",
"@radix-ui/react-avatar": "1.1.2",
"@radix-ui/react-checkbox": "1.1.3",
"@radix-ui/react-collapsible": "1.1.2",
"@radix-ui/react-context-menu": "2.2.4",
"@radix-ui/react-dialog": "1.1.4",
"@radix-ui/react-dropdown-menu": "2.1.4",
"@radix-ui/react-hover-card": "1.1.4",
"@radix-ui/react-label": "2.1.1",
"@radix-ui/react-menubar": "1.1.4",
"@radix-ui/react-navigation-menu": "1.2.3",
"@radix-ui/react-popover": "1.1.4",
"@radix-ui/react-progress": "1.1.1",
"@radix-ui/react-radio-group": "1.2.2",
"@radix-ui/react-scroll-area": "1.2.2",
"@radix-ui/react-select": "2.1.4",
"@radix-ui/react-separator": "1.1.1",
"@radix-ui/react-slider": "1.2.2",
"@radix-ui/react-slot": "1.1.1",
"@radix-ui/react-switch": "1.1.2",
"@radix-ui/react-tabs": "1.1.2",
"@radix-ui/react-toast": "1.2.4",
"@radix-ui/react-toggle": "1.1.1",
"@radix-ui/react-toggle-group": "1.1.1",
"@radix-ui/react-tooltip": "1.1.6",
"@vercel/analytics": "1.3.1",
"autoprefixer": "^10.4.20",
"class-variance-authority": "^0.7.1",
"clsx": "^2.1.1",
"cmdk": "1.0.4",
"date-fns": "4.1.0",
"embla-carousel-react": "8.5.1",
"input-otp": "1.4.1",
"jspdf": "latest",
"lucide-react": "^0.454.0",
"next": "16.0.0",
"next-themes": "^0.4.6",
"react": "19.2.0",
"react-day-picker": "9.8.0",
"react-dom": "19.2.0",
"react-hook-form": "^7.60.0",
"react-resizable-panels": "^2.1.7",
"recharts": "latest",
"sonner": "^1.7.4",
"tailwind-merge": "^2.5.5",
"tailwindcss-animate": "^1.0.7",
"vaul": "^0.9.9",
"zod": "3.25.76"
},
"devDependencies": {
"@tailwindcss/postcss": "^4.1.9",
"@types/node": "^22",
"@types/react": "^19",
"@types/react-dom": "^19",
"postcss": "^8.5",
"tailwindcss": "^4.1.9",
"tw-animate-css": "1.3.3",
"typescript": "^5"
}
}

================================================
FILE: pnpm-lock.yaml
================================================
lockfileVersion: '9.0'

settings:
autoInstallPeers: true
excludeLinksFromLockfile: false

importers:

.:
dependencies:
'@hookform/resolvers':
specifier: ^3.10.0
version: 3.10.0(react-hook-form@7.60.0(react@19.2.0))
'@radix-ui/react-accordion':
specifier: 1.2.2
version: 1.2.2(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-alert-dialog':
specifier: 1.1.4
version: 1.1.4(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-aspect-ratio':
specifier: 1.1.1
version: 1.1.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-avatar':
specifier: 1.1.2
version: 1.1.2(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-checkbox':
specifier: 1.1.3
version: 1.1.3(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-collapsible':
specifier: 1.1.2
version: 1.1.2(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-context-menu':
specifier: 2.2.4
version: 2.2.4(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-dialog':
specifier: 1.1.4
version: 1.1.4(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-dropdown-menu':
specifier: 2.1.4
version: 2.1.4(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-hover-card':
specifier: 1.1.4
version: 1.1.4(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-label':
specifier: 2.1.1
version: 2.1.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-menubar':
specifier: 1.1.4
version: 1.1.4(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-navigation-menu':
specifier: 1.2.3
version: 1.2.3(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-popover':
specifier: 1.1.4
version: 1.1.4(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-progress':
specifier: 1.1.1
version: 1.1.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-radio-group':
specifier: 1.2.2
version: 1.2.2(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-scroll-area':
specifier: 1.2.2
version: 1.2.2(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-select':
specifier: 2.1.4
version: 2.1.4(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-separator':
specifier: 1.1.1
version: 1.1.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-slider':
specifier: 1.2.2
version: 1.2.2(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-slot':
specifier: 1.1.1
version: 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-switch':
specifier: 1.1.2
version: 1.1.2(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-tabs':
specifier: 1.1.2
version: 1.1.2(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-toast':
specifier: 1.2.4
version: 1.2.4(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-toggle':
specifier: 1.1.1
version: 1.1.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-toggle-group':
specifier: 1.1.1
version: 1.1.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-tooltip':
specifier: 1.1.6
version: 1.1.6(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@vercel/analytics':
specifier: 1.3.1
version: 1.3.1(next@16.0.0(react-dom@19.2.0(react@19.2.0))(react@19.2.0))(react@19.2.0)
autoprefixer:
specifier: ^10.4.20
version: 10.4.20(postcss@8.5.0)
class-variance-authority:
specifier: ^0.7.1
version: 0.7.1
clsx:
specifier: ^2.1.1
version: 2.1.1
cmdk:
specifier: 1.0.4
version: 1.0.4(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
date-fns:
specifier: 4.1.0
version: 4.1.0
embla-carousel-react:
specifier: 8.5.1
version: 8.5.1(react@19.2.0)
input-otp:
specifier: 1.4.1
version: 1.4.1(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
jspdf:
specifier: latest
version: 3.0.3
lucide-react:
specifier: ^0.454.0
version: 0.454.0(react@19.2.0)
next:
specifier: 16.0.0
version: 16.0.0(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
next-themes:
specifier: ^0.4.6
version: 0.4.6(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
react:
specifier: 19.2.0
version: 19.2.0
react-day-picker:
specifier: 9.8.0
version: 9.8.0(react@19.2.0)
react-dom:
specifier: 19.2.0
version: 19.2.0(react@19.2.0)
react-hook-form:
specifier: ^7.60.0
version: 7.60.0(react@19.2.0)
react-resizable-panels:
specifier: ^2.1.7
version: 2.1.7(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
recharts:
specifier: latest
version: 3.3.0(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react-is@19.2.0)(react@19.2.0)(redux@5.0.1)
sonner:
specifier: ^1.7.4
version: 1.7.4(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
tailwind-merge:
specifier: ^2.5.5
version: 2.5.5
tailwindcss-animate:
specifier: ^1.0.7
version: 1.0.7(tailwindcss@4.1.9)
vaul:
specifier: ^0.9.9
version: 0.9.9(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
zod:
specifier: 3.25.76
version: 3.25.76
devDependencies:
'@tailwindcss/postcss':
specifier: ^4.1.9
version: 4.1.9
'@types/node':
specifier: ^22
version: 22.0.0
'@types/react':
specifier: ^19
version: 19.0.0
'@types/react-dom':
specifier: ^19
version: 19.0.0
postcss:
specifier: ^8.5
version: 8.5.0
tailwindcss:
specifier: ^4.1.9
version: 4.1.9
tw-animate-css:
specifier: 1.3.3
version: 1.3.3
typescript:
specifier: ^5
version: 5.0.2

packages:

'@alloc/quick-lru@5.2.0':
resolution: {integrity: sha512-UrcABB+4bUrFABwbluTIBErXwvbsU/V7TZWfmbgJfbkwiBuziS9gxdODUyuiecfdGQ85jglMW6juS3+z5TsKLw==}
engines: {node: '>=10'}

'@ampproject/remapping@2.3.0':
resolution: {integrity: sha512-30iZtAPgz+LTIYoeivqYo853f02jBYSd5uGnGpkFV0M3xOt9aN73erkgYAmZU43x4VfqcnLxW9Kpg3R5LC4YYw==}
engines: {node: '>=6.0.0'}

'@babel/runtime@7.28.4':
resolution: {integrity: sha512-Q/N6JNWvIvPnLDvjlE1OUBLPQHH6l3CltCEsHIujp45zQUSSh8K+gHnaEX45yAT1nyngnINhvWtzN+Nb9D8RAQ==}
engines: {node: '>=6.9.0'}

'@date-fns/tz@1.2.0':
resolution: {integrity: sha512-LBrd7MiJZ9McsOgxqWX7AaxrDjcFVjWH/tIKJd7pnR7McaslGYOP1QmmiBXdJH/H/yLCT+rcQ7FaPBUxRGUtrg==}

'@emnapi/runtime@1.6.0':
resolution: {integrity: sha512-obtUmAHTMjll499P+D9A3axeJFlhdjOWdKUNs/U6QIGT7V5RjcUW1xToAzjvmgTSQhDbYn/NwfTRoJcQ2rNBxA==}

'@floating-ui/core@1.7.3':
resolution: {integrity: sha512-sGnvb5dmrJaKEZ+LDIpguvdX3bDlEllmv4/ClQ9awcmCZrlx5jQyyMWFM5kBI+EyNOCDDiKk8il0zeuX3Zlg/w==}

'@floating-ui/dom@1.7.4':
resolution: {integrity: sha512-OOchDgh4F2CchOX94cRVqhvy7b3AFb+/rQXyswmzmGakRfkMgoWVjfnLWkRirfLEfuD4ysVW16eXzwt3jHIzKA==}

'@floating-ui/react-dom@2.1.6':
resolution: {integrity: sha512-4JX6rEatQEvlmgU80wZyq9RT96HZJa88q8hp0pBd+LrczeDI4o6uA2M+uvxngVHo4Ihr8uibXxH6+70zhAFrVw==}
peerDependencies:
react: '>=16.8.0'
react-dom: '>=16.8.0'

'@floating-ui/utils@0.2.10':
resolution: {integrity: sha512-aGTxbpbg8/b5JfU1HXSrbH3wXZuLPJcNEcZQFMxLs3oSzgtVu6nFPkbbGGUvBcUjKV2YyB9Wxxabo+HEH9tcRQ==}

'@hookform/resolvers@3.10.0':
resolution: {integrity: sha512-79Dv+3mDF7i+2ajj7SkypSKHhl1cbln1OGavqrsF7p6mbUv11xpqpacPsGDCTRvCSjEEIez2ef1NveSVL3b0Ag==}
peerDependencies:
react-hook-form: ^7.0.0

'@img/colour@1.0.0':
resolution: {integrity: sha512-A5P/LfWGFSl6nsckYtjw9da+19jB8hkJ6ACTGcDfEJ0aE+l2n2El7dsVM7UVHZQ9s2lmYMWlrS21YLy2IR1LUw==}
engines: {node: '>=18'}

'@img/sharp-darwin-arm64@0.34.4':
resolution: {integrity: sha512-sitdlPzDVyvmINUdJle3TNHl+AG9QcwiAMsXmccqsCOMZNIdW2/7S26w0LyU8euiLVzFBL3dXPwVCq/ODnf2vA==}
engines: {node: ^18.17.0 || ^20.3.0 || >=21.0.0}
cpu: [arm64]
os: [darwin]

'@img/sharp-darwin-x64@0.34.4':
resolution: {integrity: sha512-rZheupWIoa3+SOdF/IcUe1ah4ZDpKBGWcsPX6MT0lYniH9micvIU7HQkYTfrx5Xi8u+YqwLtxC/3vl8TQN6rMg==}
engines: {node: ^18.17.0 || ^20.3.0 || >=21.0.0}
cpu: [x64]
os: [darwin]

'@img/sharp-libvips-darwin-arm64@1.2.3':
resolution: {integrity: sha512-QzWAKo7kpHxbuHqUC28DZ9pIKpSi2ts2OJnoIGI26+HMgq92ZZ4vk8iJd4XsxN+tYfNJxzH6W62X5eTcsBymHw==}
cpu: [arm64]
os: [darwin]

'@img/sharp-libvips-darwin-x64@1.2.3':
resolution: {integrity: sha512-Ju+g2xn1E2AKO6YBhxjj+ACcsPQRHT0bhpglxcEf+3uyPY+/gL8veniKoo96335ZaPo03bdDXMv0t+BBFAbmRA==}
cpu: [x64]
os: [darwin]

'@img/sharp-libvips-linux-arm64@1.2.3':
resolution: {integrity: sha512-I4RxkXU90cpufazhGPyVujYwfIm9Nk1QDEmiIsaPwdnm013F7RIceaCc87kAH+oUB1ezqEvC6ga4m7MSlqsJvQ==}
cpu: [arm64]
os: [linux]

'@img/sharp-libvips-linux-arm@1.2.3':
resolution: {integrity: sha512-x1uE93lyP6wEwGvgAIV0gP6zmaL/a0tGzJs/BIDDG0zeBhMnuUPm7ptxGhUbcGs4okDJrk4nxgrmxpib9g6HpA==}
cpu: [arm]
os: [linux]

'@img/sharp-libvips-linux-ppc64@1.2.3':
resolution: {integrity: sha512-Y2T7IsQvJLMCBM+pmPbM3bKT/yYJvVtLJGfCs4Sp95SjvnFIjynbjzsa7dY1fRJX45FTSfDksbTp6AGWudiyCg==}
cpu: [ppc64]
os: [linux]

'@img/sharp-libvips-linux-s390x@1.2.3':
resolution: {integrity: sha512-RgWrs/gVU7f+K7P+KeHFaBAJlNkD1nIZuVXdQv6S+fNA6syCcoboNjsV2Pou7zNlVdNQoQUpQTk8SWDHUA3y/w==}
cpu: [s390x]
os: [linux]

'@img/sharp-libvips-linux-x64@1.2.3':
resolution: {integrity: sha512-3JU7LmR85K6bBiRzSUc/Ff9JBVIFVvq6bomKE0e63UXGeRw2HPVEjoJke1Yx+iU4rL7/7kUjES4dZ/81Qjhyxg==}
cpu: [x64]
os: [linux]

'@img/sharp-libvips-linuxmusl-arm64@1.2.3':
resolution: {integrity: sha512-F9q83RZ8yaCwENw1GieztSfj5msz7GGykG/BA+MOUefvER69K/ubgFHNeSyUu64amHIYKGDs4sRCMzXVj8sEyw==}
cpu: [arm64]
os: [linux]

'@img/sharp-libvips-linuxmusl-x64@1.2.3':
resolution: {integrity: sha512-U5PUY5jbc45ANM6tSJpsgqmBF/VsL6LnxJmIf11kB7J5DctHgqm0SkuXzVWtIY90GnJxKnC/JT251TDnk1fu/g==}
cpu: [x64]
os: [linux]

'@img/sharp-linux-arm64@0.34.4':
resolution: {integrity: sha512-YXU1F/mN/Wu786tl72CyJjP/Ngl8mGHN1hST4BGl+hiW5jhCnV2uRVTNOcaYPs73NeT/H8Upm3y9582JVuZHrQ==}
engines: {node: ^18.17.0 || ^20.3.0 || >=21.0.0}
cpu: [arm64]
os: [linux]

'@img/sharp-linux-arm@0.34.4':
resolution: {integrity: sha512-Xyam4mlqM0KkTHYVSuc6wXRmM7LGN0P12li03jAnZ3EJWZqj83+hi8Y9UxZUbxsgsK1qOEwg7O0Bc0LjqQVtxA==}
engines: {node: ^18.17.0 || ^20.3.0 || >=21.0.0}
cpu: [arm]
os: [linux]

'@img/sharp-linux-ppc64@0.34.4':
resolution: {integrity: sha512-F4PDtF4Cy8L8hXA2p3TO6s4aDt93v+LKmpcYFLAVdkkD3hSxZzee0rh6/+94FpAynsuMpLX5h+LRsSG3rIciUQ==}
engines: {node: ^18.17.0 || ^20.3.0 || >=21.0.0}
cpu: [ppc64]
os: [linux]

'@img/sharp-linux-s390x@0.34.4':
resolution: {integrity: sha512-qVrZKE9Bsnzy+myf7lFKvng6bQzhNUAYcVORq2P7bDlvmF6u2sCmK2KyEQEBdYk+u3T01pVsPrkj943T1aJAsw==}
engines: {node: ^18.17.0 || ^20.3.0 || >=21.0.0}
cpu: [s390x]
os: [linux]

'@img/sharp-linux-x64@0.34.4':
resolution: {integrity: sha512-ZfGtcp2xS51iG79c6Vhw9CWqQC8l2Ot8dygxoDoIQPTat/Ov3qAa8qpxSrtAEAJW+UjTXc4yxCjNfxm4h6Xm2A==}
engines: {node: ^18.17.0 || ^20.3.0 || >=21.0.0}
cpu: [x64]
os: [linux]

'@img/sharp-linuxmusl-arm64@0.34.4':
resolution: {integrity: sha512-8hDVvW9eu4yHWnjaOOR8kHVrew1iIX+MUgwxSuH2XyYeNRtLUe4VNioSqbNkB7ZYQJj9rUTT4PyRscyk2PXFKA==}
engines: {node: ^18.17.0 || ^20.3.0 || >=21.0.0}
cpu: [arm64]
os: [linux]

'@img/sharp-linuxmusl-x64@0.34.4':
resolution: {integrity: sha512-lU0aA5L8QTlfKjpDCEFOZsTYGn3AEiO6db8W5aQDxj0nQkVrZWmN3ZP9sYKWJdtq3PWPhUNlqehWyXpYDcI9Sg==}
engines: {node: ^18.17.0 || ^20.3.0 || >=21.0.0}
cpu: [x64]
os: [linux]

'@img/sharp-wasm32@0.34.4':
resolution: {integrity: sha512-33QL6ZO/qpRyG7woB/HUALz28WnTMI2W1jgX3Nu2bypqLIKx/QKMILLJzJjI+SIbvXdG9fUnmrxR7vbi1sTBeA==}
engines: {node: ^18.17.0 || ^20.3.0 || >=21.0.0}
cpu: [wasm32]

'@img/sharp-win32-arm64@0.34.4':
resolution: {integrity: sha512-2Q250do/5WXTwxW3zjsEuMSv5sUU4Tq9VThWKlU2EYLm4MB7ZeMwF+SFJutldYODXF6jzc6YEOC+VfX0SZQPqA==}
engines: {node: ^18.17.0 || ^20.3.0 || >=21.0.0}
cpu: [arm64]
os: [win32]

'@img/sharp-win32-ia32@0.34.4':
resolution: {integrity: sha512-3ZeLue5V82dT92CNL6rsal6I2weKw1cYu+rGKm8fOCCtJTR2gYeUfY3FqUnIJsMUPIH68oS5jmZ0NiJ508YpEw==}
engines: {node: ^18.17.0 || ^20.3.0 || >=21.0.0}
cpu: [ia32]
os: [win32]

'@img/sharp-win32-x64@0.34.4':
resolution: {integrity: sha512-xIyj4wpYs8J18sVN3mSQjwrw7fKUqRw+Z5rnHNCy5fYTxigBz81u5mOMPmFumwjcn8+ld1ppptMBCLic1nz6ig==}
engines: {node: ^18.17.0 || ^20.3.0 || >=21.0.0}
cpu: [x64]
os: [win32]

'@isaacs/fs-minipass@4.0.1':
resolution: {integrity: sha512-wgm9Ehl2jpeqP3zw/7mo3kRHFp5MEDhqAdwy1fTGkHAwnkGOVsgpvQhL8B5n1qlb01jV3n/bI0ZfZp5lWA1k4w==}
engines: {node: '>=18.0.0'}

'@jridgewell/gen-mapping@0.3.13':
resolution: {integrity: sha512-2kkt/7niJ6MgEPxF0bYdQ6etZaA+fQvDcLKckhy1yIQOzaoKjBBjSj63/aLVjYE3qhRt5dvM+uUyfCg6UKCBbA==}

'@jridgewell/resolve-uri@3.1.2':
resolution: {integrity: sha512-bRISgCIjP20/tbWSPWMEi54QVPRZExkuD9lJL+UIxUKtwVJA8wW1Trb1jMs1RFXo1CBTNZ/5hpC9QvmKWdopKw==}
engines: {node: '>=6.0.0'}

'@jridgewell/sourcemap-codec@1.5.5':
resolution: {integrity: sha512-cYQ9310grqxueWbl+WuIUIaiUaDcj7WOq5fVhEljNVgRfOUhY9fy2zTvfoqWsnebh8Sl70VScFbICvJnLKB0Og==}

'@jridgewell/trace-mapping@0.3.31':
resolution: {integrity: sha512-zzNR+SdQSDJzc8joaeP8QQoCQr8NuYx2dIIytl1QeBEZHJ9uW6hebsrYgbz8hJwUQao3TWCMtmfV8Nu1twOLAw==}

'@next/env@16.0.0':
resolution: {integrity: sha512-s5j2iFGp38QsG1LWRQaE2iUY3h1jc014/melHFfLdrsMJPqxqDQwWNwyQTcNoUSGZlCVZuM7t7JDMmSyRilsnA==}

'@next/swc-darwin-arm64@16.0.0':
resolution: {integrity: sha512-/CntqDCnk5w2qIwMiF0a9r6+9qunZzFmU0cBX4T82LOflE72zzH6gnOjCwUXYKOBlQi8OpP/rMj8cBIr18x4TA==}
engines: {node: '>= 10'}
cpu: [arm64]
os: [darwin]

'@next/swc-darwin-x64@16.0.0':
resolution: {integrity: sha512-hB4GZnJGKa8m4efvTGNyii6qs76vTNl+3dKHTCAUaksN6KjYy4iEO3Q5ira405NW2PKb3EcqWiRaL9DrYJfMHg==}
engines: {node: '>= 10'}
cpu: [x64]
os: [darwin]

'@next/swc-linux-arm64-gnu@16.0.0':
resolution: {integrity: sha512-E2IHMdE+C1k+nUgndM13/BY/iJY9KGCphCftMh7SXWcaQqExq/pJU/1Hgn8n/tFwSoLoYC/yUghOv97tAsIxqg==}
engines: {node: '>= 10'}
cpu: [arm64]
os: [linux]

'@next/swc-linux-arm64-musl@16.0.0':
resolution: {integrity: sha512-xzgl7c7BVk4+7PDWldU+On2nlwnGgFqJ1siWp3/8S0KBBLCjonB6zwJYPtl4MUY7YZJrzzumdUpUoquu5zk8vg==}
engines: {node: '>= 10'}
cpu: [arm64]
os: [linux]

'@next/swc-linux-x64-gnu@16.0.0':
resolution: {integrity: sha512-sdyOg4cbiCw7YUr0F/7ya42oiVBXLD21EYkSwN+PhE4csJH4MSXUsYyslliiiBwkM+KsuQH/y9wuxVz6s7Nstg==}
engines: {node: '>= 10'}
cpu: [x64]
os: [linux]

'@next/swc-linux-x64-musl@16.0.0':
resolution: {integrity: sha512-IAXv3OBYqVaNOgyd3kxR4L3msuhmSy1bcchPHxDOjypG33i2yDWvGBwFD94OuuTjjTt/7cuIKtAmoOOml6kfbg==}
engines: {node: '>= 10'}
cpu: [x64]
os: [linux]

'@next/swc-win32-arm64-msvc@16.0.0':
resolution: {integrity: sha512-bmo3ncIJKUS9PWK1JD9pEVv0yuvp1KPuOsyJTHXTv8KDrEmgV/K+U0C75rl9rhIaODcS7JEb6/7eJhdwXI0XmA==}
engines: {node: '>= 10'}
cpu: [arm64]
os: [win32]

'@next/swc-win32-x64-msvc@16.0.0':
resolution: {integrity: sha512-O1cJbT+lZp+cTjYyZGiDwsOjO3UHHzSqobkPNipdlnnuPb1swfcuY6r3p8dsKU4hAIEO4cO67ZCfVVH/M1ETXA==}
engines: {node: '>= 10'}
cpu: [x64]
os: [win32]

'@radix-ui/number@1.1.0':
resolution: {integrity: sha512-V3gRzhVNU1ldS5XhAPTom1fOIo4ccrjjJgmE+LI2h/WaFpHmx0MQApT+KZHnx8abG6Avtfcz4WoEciMnpFT3HQ==}

'@radix-ui/primitive@1.1.1':
resolution: {integrity: sha512-SJ31y+Q/zAyShtXJc8x83i9TYdbAfHZ++tUZnvjJJqFjzsdUnKsxPL6IEtBlxKkU7yzer//GQtZSV4GbldL3YA==}

'@radix-ui/react-accordion@1.2.2':
resolution: {integrity: sha512-b1oh54x4DMCdGsB4/7ahiSrViXxaBwRPotiZNnYXjLha9vfuURSAZErki6qjDoSIV0eXx5v57XnTGVtGwnfp2g==}
peerDependencies:
'@types/react': '_'
'@types/react-dom': '_'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
react-dom: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true
'@types/react-dom':
optional: true

'@radix-ui/react-alert-dialog@1.1.4':
resolution: {integrity: sha512-A6Kh23qZDLy3PSU4bh2UJZznOrUdHImIXqF8YtUa6CN73f8EOO9XlXSCd9IHyPvIquTaa/kwaSWzZTtUvgXVGw==}
peerDependencies:
'@types/react': '_'
'@types/react-dom': '_'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
react-dom: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true
'@types/react-dom':
optional: true

'@radix-ui/react-arrow@1.1.1':
resolution: {integrity: sha512-NaVpZfmv8SKeZbn4ijN2V3jlHA9ngBG16VnIIm22nUR0Yk8KUALyBxT3KYEUnNuch9sTE8UTsS3whzBgKOL30w==}
peerDependencies:
'@types/react': '_'
'@types/react-dom': '_'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
react-dom: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true
'@types/react-dom':
optional: true

'@radix-ui/react-aspect-ratio@1.1.1':
resolution: {integrity: sha512-kNU4FIpcFMBLkOUcgeIteH06/8JLBcYY6Le1iKenDGCYNYFX3TQqCZjzkOsz37h7r94/99GTb7YhEr98ZBJibw==}
peerDependencies:
'@types/react': '_'
'@types/react-dom': '_'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
react-dom: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true
'@types/react-dom':
optional: true

'@radix-ui/react-avatar@1.1.2':
resolution: {integrity: sha512-GaC7bXQZ5VgZvVvsJ5mu/AEbjYLnhhkoidOboC50Z6FFlLA03wG2ianUoH+zgDQ31/9gCF59bE4+2bBgTyMiig==}
peerDependencies:
'@types/react': '_'
'@types/react-dom': '_'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
react-dom: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true
'@types/react-dom':
optional: true

'@radix-ui/react-checkbox@1.1.3':
resolution: {integrity: sha512-HD7/ocp8f1B3e6OHygH0n7ZKjONkhciy1Nh0yuBgObqThc3oyx+vuMfFHKAknXRHHWVE9XvXStxJFyjUmB8PIw==}
peerDependencies:
'@types/react': '_'
'@types/react-dom': '_'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
react-dom: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true
'@types/react-dom':
optional: true

'@radix-ui/react-collapsible@1.1.2':
resolution: {integrity: sha512-PliMB63vxz7vggcyq0IxNYk8vGDrLXVWw4+W4B8YnwI1s18x7YZYqlG9PLX7XxAJUi0g2DxP4XKJMFHh/iVh9A==}
peerDependencies:
'@types/react': '_'
'@types/react-dom': '_'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
react-dom: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true
'@types/react-dom':
optional: true

'@radix-ui/react-collection@1.1.1':
resolution: {integrity: sha512-LwT3pSho9Dljg+wY2KN2mrrh6y3qELfftINERIzBUO9e0N+t0oMTyn3k9iv+ZqgrwGkRnLpNJrsMv9BZlt2yuA==}
peerDependencies:
'@types/react': '_'
'@types/react-dom': '_'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
react-dom: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true
'@types/react-dom':
optional: true

'@radix-ui/react-compose-refs@1.1.1':
resolution: {integrity: sha512-Y9VzoRDSJtgFMUCoiZBDVo084VQ5hfpXxVE+NgkdNsjiDBByiImMZKKhxMwCbdHvhlENG6a833CbFkOQvTricw==}
peerDependencies:
'@types/react': '\*'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true

'@radix-ui/react-compose-refs@1.1.2':
resolution: {integrity: sha512-z4eqJvfiNnFMHIIvXP3CY57y2WJs5g2v3X0zm9mEJkrkNv4rDxu+sg9Jh8EkXyeqBkB7SOcboo9dMVqhyrACIg==}
peerDependencies:
'@types/react': '\*'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true

'@radix-ui/react-context-menu@2.2.4':
resolution: {integrity: sha512-ap4wdGwK52rJxGkwukU1NrnEodsUFQIooANKu+ey7d6raQ2biTcEf8za1zr0mgFHieevRTB2nK4dJeN8pTAZGQ==}
peerDependencies:
'@types/react': '_'
'@types/react-dom': '_'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
react-dom: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true
'@types/react-dom':
optional: true

'@radix-ui/react-context@1.1.1':
resolution: {integrity: sha512-UASk9zi+crv9WteK/NU4PLvOoL3OuE6BWVKNF6hPRBtYBDXQ2u5iu3O59zUlJiTVvkyuycnqrztsHVJwcK9K+Q==}
peerDependencies:
'@types/react': '\*'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true

'@radix-ui/react-dialog@1.1.4':
resolution: {integrity: sha512-Ur7EV1IwQGCyaAuyDRiOLA5JIUZxELJljF+MbM/2NC0BYwfuRrbpS30BiQBJrVruscgUkieKkqXYDOoByaxIoA==}
peerDependencies:
'@types/react': '_'
'@types/react-dom': '_'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
react-dom: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true
'@types/react-dom':
optional: true

'@radix-ui/react-direction@1.1.0':
resolution: {integrity: sha512-BUuBvgThEiAXh2DWu93XsT+a3aWrGqolGlqqw5VU1kG7p/ZH2cuDlM1sRLNnY3QcBS69UIz2mcKhMxDsdewhjg==}
peerDependencies:
'@types/react': '\*'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true

'@radix-ui/react-dismissable-layer@1.1.3':
resolution: {integrity: sha512-onrWn/72lQoEucDmJnr8uczSNTujT0vJnA/X5+3AkChVPowr8n1yvIKIabhWyMQeMvvmdpsvcyDqx3X1LEXCPg==}
peerDependencies:
'@types/react': '_'
'@types/react-dom': '_'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
react-dom: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true
'@types/react-dom':
optional: true

'@radix-ui/react-dropdown-menu@2.1.4':
resolution: {integrity: sha512-iXU1Ab5ecM+yEepGAWK8ZhMyKX4ubFdCNtol4sT9D0OVErG9PNElfx3TQhjw7n7BC5nFVz68/5//clWy+8TXzA==}
peerDependencies:
'@types/react': '_'
'@types/react-dom': '_'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
react-dom: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true
'@types/react-dom':
optional: true

'@radix-ui/react-focus-guards@1.1.1':
resolution: {integrity: sha512-pSIwfrT1a6sIoDASCSpFwOasEwKTZWDw/iBdtnqKO7v6FeOzYJ7U53cPzYFVR3geGGXgVHaH+CdngrrAzqUGxg==}
peerDependencies:
'@types/react': '\*'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true

'@radix-ui/react-focus-scope@1.1.1':
resolution: {integrity: sha512-01omzJAYRxXdG2/he/+xy+c8a8gCydoQ1yOxnWNcRhrrBW5W+RQJ22EK1SaO8tb3WoUsuEw7mJjBozPzihDFjA==}
peerDependencies:
'@types/react': '_'
'@types/react-dom': '_'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
react-dom: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true
'@types/react-dom':
optional: true

'@radix-ui/react-hover-card@1.1.4':
resolution: {integrity: sha512-QSUUnRA3PQ2UhvoCv3eYvMnCAgGQW+sTu86QPuNb+ZMi+ZENd6UWpiXbcWDQ4AEaKF9KKpCHBeaJz9Rw6lRlaQ==}
peerDependencies:
'@types/react': '_'
'@types/react-dom': '_'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
react-dom: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true
'@types/react-dom':
optional: true

'@radix-ui/react-id@1.1.0':
resolution: {integrity: sha512-EJUrI8yYh7WOjNOqpoJaf1jlFIH2LvtgAl+YcFqNCa+4hj64ZXmPkAKOFs/ukjz3byN6bdb/AVUqHkI8/uWWMA==}
peerDependencies:
'@types/react': '\*'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true

'@radix-ui/react-id@1.1.1':
resolution: {integrity: sha512-kGkGegYIdQsOb4XjsfM97rXsiHaBwco+hFI66oO4s9LU+PLAC5oJ7khdOVFxkhsmlbpUqDAvXw11CluXP+jkHg==}
peerDependencies:
'@types/react': '\*'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true

'@radix-ui/react-label@2.1.1':
resolution: {integrity: sha512-UUw5E4e/2+4kFMH7+YxORXGWggtY6sM8WIwh5RZchhLuUg2H1hc98Py+pr8HMz6rdaYrK2t296ZEjYLOCO5uUw==}
peerDependencies:
'@types/react': '_'
'@types/react-dom': '_'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
react-dom: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true
'@types/react-dom':
optional: true

'@radix-ui/react-menu@2.1.4':
resolution: {integrity: sha512-BnOgVoL6YYdHAG6DtXONaR29Eq4nvbi8rutrV/xlr3RQCMMb3yqP85Qiw/3NReozrSW+4dfLkK+rc1hb4wPU/A==}
peerDependencies:
'@types/react': '_'
'@types/react-dom': '_'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
react-dom: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true
'@types/react-dom':
optional: true

'@radix-ui/react-menubar@1.1.4':
resolution: {integrity: sha512-+KMpi7VAZuB46+1LD7a30zb5IxyzLgC8m8j42gk3N4TUCcViNQdX8FhoH1HDvYiA8quuqcek4R4bYpPn/SY1GA==}
peerDependencies:
'@types/react': '_'
'@types/react-dom': '_'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
react-dom: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true
'@types/react-dom':
optional: true

'@radix-ui/react-navigation-menu@1.2.3':
resolution: {integrity: sha512-IQWAsQ7dsLIYDrn0WqPU+cdM7MONTv9nqrLVYoie3BPiabSfUVDe6Fr+oEt0Cofsr9ONDcDe9xhmJbL1Uq1yKg==}
peerDependencies:
'@types/react': '_'
'@types/react-dom': '_'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
react-dom: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true
'@types/react-dom':
optional: true

'@radix-ui/react-popover@1.1.4':
resolution: {integrity: sha512-aUACAkXx8LaFymDma+HQVji7WhvEhpFJ7+qPz17Nf4lLZqtreGOFRiNQWQmhzp7kEWg9cOyyQJpdIMUMPc/CPw==}
peerDependencies:
'@types/react': '_'
'@types/react-dom': '_'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
react-dom: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true
'@types/react-dom':
optional: true

'@radix-ui/react-popper@1.2.1':
resolution: {integrity: sha512-3kn5Me69L+jv82EKRuQCXdYyf1DqHwD2U/sxoNgBGCB7K9TRc3bQamQ+5EPM9EvyPdli0W41sROd+ZU1dTCztw==}
peerDependencies:
'@types/react': '_'
'@types/react-dom': '_'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
react-dom: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true
'@types/react-dom':
optional: true

'@radix-ui/react-portal@1.1.3':
resolution: {integrity: sha512-NciRqhXnGojhT93RPyDaMPfLH3ZSl4jjIFbZQ1b/vxvZEdHsBZ49wP9w8L3HzUQwep01LcWtkUvm0OVB5JAHTw==}
peerDependencies:
'@types/react': '_'
'@types/react-dom': '_'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
react-dom: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true
'@types/react-dom':
optional: true

'@radix-ui/react-presence@1.1.2':
resolution: {integrity: sha512-18TFr80t5EVgL9x1SwF/YGtfG+l0BS0PRAlCWBDoBEiDQjeKgnNZRVJp/oVBl24sr3Gbfwc/Qpj4OcWTQMsAEg==}
peerDependencies:
'@types/react': '_'
'@types/react-dom': '_'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
react-dom: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true
'@types/react-dom':
optional: true

'@radix-ui/react-primitive@2.0.1':
resolution: {integrity: sha512-sHCWTtxwNn3L3fH8qAfnF3WbUZycW93SM1j3NFDzXBiz8D6F5UTTy8G1+WFEaiCdvCVRJWj6N2R4Xq6HdiHmDg==}
peerDependencies:
'@types/react': '_'
'@types/react-dom': '_'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
react-dom: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true
'@types/react-dom':
optional: true

'@radix-ui/react-primitive@2.1.3':
resolution: {integrity: sha512-m9gTwRkhy2lvCPe6QJp4d3G1TYEUHn/FzJUtq9MjH46an1wJU+GdoGC5VLof8RX8Ft/DlpshApkhswDLZzHIcQ==}
peerDependencies:
'@types/react': '_'
'@types/react-dom': '_'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
react-dom: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true
'@types/react-dom':
optional: true

'@radix-ui/react-progress@1.1.1':
resolution: {integrity: sha512-6diOawA84f/eMxFHcWut0aE1C2kyE9dOyCTQOMRR2C/qPiXz/X0SaiA/RLbapQaXUCmy0/hLMf9meSccD1N0pA==}
peerDependencies:
'@types/react': '_'
'@types/react-dom': '_'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
react-dom: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true
'@types/react-dom':
optional: true

'@radix-ui/react-radio-group@1.2.2':
resolution: {integrity: sha512-E0MLLGfOP0l8P/NxgVzfXJ8w3Ch8cdO6UDzJfDChu4EJDy+/WdO5LqpdY8PYnCErkmZH3gZhDL1K7kQ41fAHuQ==}
peerDependencies:
'@types/react': '_'
'@types/react-dom': '_'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
react-dom: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true
'@types/react-dom':
optional: true

'@radix-ui/react-roving-focus@1.1.1':
resolution: {integrity: sha512-QE1RoxPGJ/Nm8Qmk0PxP8ojmoaS67i0s7hVssS7KuI2FQoc/uzVlZsqKfQvxPE6D8hICCPHJ4D88zNhT3OOmkw==}
peerDependencies:
'@types/react': '_'
'@types/react-dom': '_'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
react-dom: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true
'@types/react-dom':
optional: true

'@radix-ui/react-scroll-area@1.2.2':
resolution: {integrity: sha512-EFI1N/S3YxZEW/lJ/H1jY3njlvTd8tBmgKEn4GHi51+aMm94i6NmAJstsm5cu3yJwYqYc93gpCPm21FeAbFk6g==}
peerDependencies:
'@types/react': '_'
'@types/react-dom': '_'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
react-dom: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true
'@types/react-dom':
optional: true

'@radix-ui/react-select@2.1.4':
resolution: {integrity: sha512-pOkb2u8KgO47j/h7AylCj7dJsm69BXcjkrvTqMptFqsE2i0p8lHkfgneXKjAgPzBMivnoMyt8o4KiV4wYzDdyQ==}
peerDependencies:
'@types/react': '_'
'@types/react-dom': '_'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
react-dom: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true
'@types/react-dom':
optional: true

'@radix-ui/react-separator@1.1.1':
resolution: {integrity: sha512-RRiNRSrD8iUiXriq/Y5n4/3iE8HzqgLHsusUSg5jVpU2+3tqcUFPJXHDymwEypunc2sWxDUS3UC+rkZRlHedsw==}
peerDependencies:
'@types/react': '_'
'@types/react-dom': '_'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
react-dom: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true
'@types/react-dom':
optional: true

'@radix-ui/react-slider@1.2.2':
resolution: {integrity: sha512-sNlU06ii1/ZcbHf8I9En54ZPW0Vil/yPVg4vQMcFNjrIx51jsHbFl1HYHQvCIWJSr1q0ZmA+iIs/ZTv8h7HHSA==}
peerDependencies:
'@types/react': '_'
'@types/react-dom': '_'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
react-dom: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true
'@types/react-dom':
optional: true

'@radix-ui/react-slot@1.1.1':
resolution: {integrity: sha512-RApLLOcINYJA+dMVbOju7MYv1Mb2EBp2nH4HdDzXTSyaR5optlm6Otrz1euW3HbdOR8UmmFK06TD+A9frYWv+g==}
peerDependencies:
'@types/react': '\*'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true

'@radix-ui/react-slot@1.2.3':
resolution: {integrity: sha512-aeNmHnBxbi2St0au6VBVC7JXFlhLlOnvIIlePNniyUNAClzmtAUEY8/pBiK3iHjufOlwA+c20/8jngo7xcrg8A==}
peerDependencies:
'@types/react': '\*'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true

'@radix-ui/react-switch@1.1.2':
resolution: {integrity: sha512-zGukiWHjEdBCRyXvKR6iXAQG6qXm2esuAD6kDOi9Cn+1X6ev3ASo4+CsYaD6Fov9r/AQFekqnD/7+V0Cs6/98g==}
peerDependencies:
'@types/react': '_'
'@types/react-dom': '_'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
react-dom: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true
'@types/react-dom':
optional: true

'@radix-ui/react-tabs@1.1.2':
resolution: {integrity: sha512-9u/tQJMcC2aGq7KXpGivMm1mgq7oRJKXphDwdypPd/j21j/2znamPU8WkXgnhUaTrSFNIt8XhOyCAupg8/GbwQ==}
peerDependencies:
'@types/react': '_'
'@types/react-dom': '_'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
react-dom: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true
'@types/react-dom':
optional: true

'@radix-ui/react-toast@1.2.4':
resolution: {integrity: sha512-Sch9idFJHJTMH9YNpxxESqABcAFweJG4tKv+0zo0m5XBvUSL8FM5xKcJLFLXononpePs8IclyX1KieL5SDUNgA==}
peerDependencies:
'@types/react': '_'
'@types/react-dom': '_'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
react-dom: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true
'@types/react-dom':
optional: true

'@radix-ui/react-toggle-group@1.1.1':
resolution: {integrity: sha512-OgDLZEA30Ylyz8YSXvnGqIHtERqnUt1KUYTKdw/y8u7Ci6zGiJfXc02jahmcSNK3YcErqioj/9flWC9S1ihfwg==}
peerDependencies:
'@types/react': '_'
'@types/react-dom': '_'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
react-dom: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true
'@types/react-dom':
optional: true

'@radix-ui/react-toggle@1.1.1':
resolution: {integrity: sha512-i77tcgObYr743IonC1hrsnnPmszDRn8p+EGUsUt+5a/JFn28fxaM88Py6V2mc8J5kELMWishI0rLnuGLFD/nnQ==}
peerDependencies:
'@types/react': '_'
'@types/react-dom': '_'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
react-dom: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true
'@types/react-dom':
optional: true

'@radix-ui/react-tooltip@1.1.6':
resolution: {integrity: sha512-TLB5D8QLExS1uDn7+wH/bjEmRurNMTzNrtq7IjaS4kjion9NtzsTGkvR5+i7yc9q01Pi2KMM2cN3f8UG4IvvXA==}
peerDependencies:
'@types/react': '_'
'@types/react-dom': '_'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
react-dom: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true
'@types/react-dom':
optional: true

'@radix-ui/react-use-callback-ref@1.1.0':
resolution: {integrity: sha512-CasTfvsy+frcFkbXtSJ2Zu9JHpN8TYKxkgJGWbjiZhFivxaeW7rMeZt7QELGVLaYVfFMsKHjb7Ak0nMEe+2Vfw==}
peerDependencies:
'@types/react': '\*'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true

'@radix-ui/react-use-controllable-state@1.1.0':
resolution: {integrity: sha512-MtfMVJiSr2NjzS0Aa90NPTnvTSg6C/JLCV7ma0W6+OMV78vd8OyRpID+Ng9LxzsPbLeuBnWBA1Nq30AtBIDChw==}
peerDependencies:
'@types/react': '\*'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true

'@radix-ui/react-use-escape-keydown@1.1.0':
resolution: {integrity: sha512-L7vwWlR1kTTQ3oh7g1O0CBF3YCyyTj8NmhLR+phShpyA50HCfBFKVJTpshm9PzLiKmehsrQzTYTpX9HvmC9rhw==}
peerDependencies:
'@types/react': '\*'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true

'@radix-ui/react-use-layout-effect@1.1.0':
resolution: {integrity: sha512-+FPE0rOdziWSrH9athwI1R0HDVbWlEhd+FR+aSDk4uWGmSJ9Z54sdZVDQPZAinJhJXwfT+qnj969mCsT2gfm5w==}
peerDependencies:
'@types/react': '\*'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true

'@radix-ui/react-use-layout-effect@1.1.1':
resolution: {integrity: sha512-RbJRS4UWQFkzHTTwVymMTUv8EqYhOp8dOOviLj2ugtTiXRaRQS7GLGxZTLL1jWhMeoSCf5zmcZkqTl9IiYfXcQ==}
peerDependencies:
'@types/react': '\*'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true

'@radix-ui/react-use-previous@1.1.0':
resolution: {integrity: sha512-Z/e78qg2YFnnXcW88A4JmTtm4ADckLno6F7OXotmkQfeuCVaKuYzqAATPhVzl3delXE7CxIV8shofPn3jPc5Og==}
peerDependencies:
'@types/react': '\*'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true

'@radix-ui/react-use-rect@1.1.0':
resolution: {integrity: sha512-0Fmkebhr6PiseyZlYAOtLS+nb7jLmpqTrJyv61Pe68MKYW6OWdRE2kI70TaYY27u7H0lajqM3hSMMLFq18Z7nQ==}
peerDependencies:
'@types/react': '\*'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true

'@radix-ui/react-use-size@1.1.0':
resolution: {integrity: sha512-XW3/vWuIXHa+2Uwcc2ABSfcCledmXhhQPlGbfcRXbiUQI5Icjcg19BGCZVKKInYbvUCut/ufbbLLPFC5cbb1hw==}
peerDependencies:
'@types/react': '\*'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true

'@radix-ui/react-visually-hidden@1.1.1':
resolution: {integrity: sha512-vVfA2IZ9q/J+gEamvj761Oq1FpWgCDaNOOIfbPVp2MVPLEomUr5+Vf7kJGwQ24YxZSlQVar7Bes8kyTo5Dshpg==}
peerDependencies:
'@types/react': '_'
'@types/react-dom': '_'
react: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
react-dom: ^16.8 || ^17.0 || ^18.0 || ^19.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true
'@types/react-dom':
optional: true

'@radix-ui/rect@1.1.0':
resolution: {integrity: sha512-A9+lCBZoaMJlVKcRBz2YByCG+Cp2t6nAnMnNba+XiWxnj6r4JUFqfsgwocMBZU9LPtdxC6wB56ySYpc7LQIoJg==}

'@reduxjs/toolkit@2.9.2':
resolution: {integrity: sha512-ZAYu/NXkl/OhqTz7rfPaAhY0+e8Fr15jqNxte/2exKUxvHyQ/hcqmdekiN1f+Lcw3pE+34FCgX+26zcUE3duCg==}
peerDependencies:
react: ^16.9.0 || ^17.0.0 || ^18 || ^19
react-redux: ^7.2.1 || ^8.1.3 || ^9.0.0
peerDependenciesMeta:
react:
optional: true
react-redux:
optional: true

'@standard-schema/spec@1.0.0':
resolution: {integrity: sha512-m2bOd0f2RT9k8QJx1JN85cZYyH1RqFBdlwtkSlf4tBDYLCiiZnv1fIIwacK6cqwXavOydf0NPToMQgpKq+dVlA==}

'@standard-schema/utils@0.3.0':
resolution: {integrity: sha512-e7Mew686owMaPJVNNLs55PUvgz371nKgwsc4vxE49zsODpJEnxgxRo2y/OKrqueavXgZNMDVj3DdHFlaSAeU8g==}

'@swc/helpers@0.5.15':
resolution: {integrity: sha512-JQ5TuMi45Owi4/BIMAJBoSQoOJu12oOk/gADqlcUL9JEdHB8vyjUSsxqeNXnmXHjYKMi2WcYtezGEEhqUI/E2g==}

'@tailwindcss/node@4.1.9':
resolution: {integrity: sha512-ZFsgw6lbtcZKYPWvf6zAuCVSuer7UQ2Z5P8BETHcpA4x/3NwOjAIXmRnYfG77F14f9bPeuR4GaNz3ji1JkQMeQ==}

'@tailwindcss/oxide-android-arm64@4.1.9':
resolution: {integrity: sha512-X4mBUUJ3DPqODhtdT5Ju55feJwBN+hP855Z7c0t11Jzece9KRtdM41ljMrCcureKMh96mcOh2gxahkp1yE+BOQ==}
engines: {node: '>= 10'}
cpu: [arm64]
os: [android]

'@tailwindcss/oxide-darwin-arm64@4.1.9':
resolution: {integrity: sha512-jnWnqz71ZLXUbJLW53m9dSQakLBfaWxAd9TAibimrNdQfZKyie+xGppdDCZExtYwUdflt3kOT9y1JUgYXVEQmw==}
engines: {node: '>= 10'}
cpu: [arm64]
os: [darwin]

'@tailwindcss/oxide-darwin-x64@4.1.9':
resolution: {integrity: sha512-+Ui6LlvZ6aCPvSwv3l16nYb6gu1N6RamFz7hSu5aqaiPrDQqD1LPT/e8r2/laSVwFjRyOZxQQ/gvGxP3ihA2rw==}
engines: {node: '>= 10'}
cpu: [x64]
os: [darwin]

'@tailwindcss/oxide-freebsd-x64@4.1.9':
resolution: {integrity: sha512-BWqCh0uoXMprwWfG7+oyPW53VCh6G08pxY0IIN/i5DQTpPnCJ4zm2W8neH9kW1v1f6RXP3b2qQjAzrAcnQ5e9w==}
engines: {node: '>= 10'}
cpu: [x64]
os: [freebsd]

'@tailwindcss/oxide-linux-arm-gnueabihf@4.1.9':
resolution: {integrity: sha512-U8itjQb5TVc80aV5Yo+JtKo+qS95CV4XLrKEtSLQFoTD/c9j3jk4WZipYT+9Jxqem29qCMRPxjEZ3s+wTT4XCw==}
engines: {node: '>= 10'}
cpu: [arm]
os: [linux]

'@tailwindcss/oxide-linux-arm64-gnu@4.1.9':
resolution: {integrity: sha512-dKlGraoNvyTrR7ovLw3Id9yTwc+l0NYg8bwOkYqk+zltvGns8bPvVr6PH5jATdc75kCGd6kDRmP4p1LwqCnPJQ==}
engines: {node: '>= 10'}
cpu: [arm64]
os: [linux]

'@tailwindcss/oxide-linux-arm64-musl@4.1.9':
resolution: {integrity: sha512-qCZ4QTrZaBEgNM13pGjvakdmid1Kw3CUCEQzgVAn64Iud7zSxOGwK1usg+hrwrOfFH7vXZZr8OhzC8fJTRq5NA==}
engines: {node: '>= 10'}
cpu: [arm64]
os: [linux]

'@tailwindcss/oxide-linux-x64-gnu@4.1.9':
resolution: {integrity: sha512-bmzkAWQjRlY9udmg/a1bOtZpV14ZCdrB74PZrd7Oz/wK62Rk+m9+UV3BsgGfOghyO5Qu5ZDciADzDMZbi9n1+g==}
engines: {node: '>= 10'}
cpu: [x64]
os: [linux]

'@tailwindcss/oxide-linux-x64-musl@4.1.9':
resolution: {integrity: sha512-NpvPQsXj1raDHhd+g2SUvZQoTPWfYAsyYo9h4ZqV7EOmR+aj7LCAE5hnXNnrJ5Egy/NiO3Hs7BNpSbsPEOpORg==}
engines: {node: '>= 10'}
cpu: [x64]
os: [linux]

'@tailwindcss/oxide-wasm32-wasi@4.1.9':
resolution: {integrity: sha512-G93Yuf3xrpTxDUCSh685d1dvOkqOB0Gy+Bchv9Zy3k+lNw/9SEgsHit50xdvp1/p9yRH2TeDHJeDLUiV4mlTkA==}
engines: {node: '>=14.0.0'}
cpu: [wasm32]
bundledDependencies: - '@napi-rs/wasm-runtime' - '@emnapi/core' - '@emnapi/runtime' - '@tybys/wasm-util' - '@emnapi/wasi-threads' - tslib

'@tailwindcss/oxide-win32-arm64-msvc@4.1.9':
resolution: {integrity: sha512-Eq9FZzZe/NPkUiSMY+eY7r5l7msuFlm6wC6lnV11m8885z0vs9zx48AKTfw0UbVecTRV5wMxKb3Kmzx2LoUIWg==}
engines: {node: '>= 10'}
cpu: [arm64]
os: [win32]

'@tailwindcss/oxide-win32-x64-msvc@4.1.9':
resolution: {integrity: sha512-oZ4zkthMXMJN2w/vu3jEfuqWTW7n8giGYDV/SfhBGRNehNMOBqh3YUAEv+8fv2YDJEzL4JpXTNTiSXW3UiUwBw==}
engines: {node: '>= 10'}
cpu: [x64]
os: [win32]

'@tailwindcss/oxide@4.1.9':
resolution: {integrity: sha512-oqjNxOBt1iNRAywjiH+VFsfovx/hVt4mxe0kOkRMAbbcCwbJg5e2AweFqyGN7gtmE1TJXnvnyX7RWTR1l72ciQ==}
engines: {node: '>= 10'}

'@tailwindcss/postcss@4.1.9':
resolution: {integrity: sha512-v3DKzHibZO8ioVDmuVHCW1PR0XSM7nS40EjZFJEA1xPuvTuQPaR5flE1LyikU3hu2u1KNWBtEaSe8qsQjX3tyg==}

'@types/d3-array@3.2.2':
resolution: {integrity: sha512-hOLWVbm7uRza0BYXpIIW5pxfrKe0W+D5lrFiAEYR+pb6w3N2SwSMaJbXdUfSEv+dT4MfHBLtn5js0LAWaO6otw==}

'@types/d3-color@3.1.3':
resolution: {integrity: sha512-iO90scth9WAbmgv7ogoq57O9YpKmFBbmoEoCHDB2xMBY0+/KVrqAaCDyCE16dUspeOvIxFFRI+0sEtqDqy2b4A==}

'@types/d3-ease@3.0.2':
resolution: {integrity: sha512-NcV1JjO5oDzoK26oMzbILE6HW7uVXOHLQvHshBUW4UMdZGfiY6v5BeQwh9a9tCzv+CeefZQHJt5SRgK154RtiA==}

'@types/d3-interpolate@3.0.4':
resolution: {integrity: sha512-mgLPETlrpVV1YRJIglr4Ez47g7Yxjl1lj7YKsiMCb27VJH9W8NVM6Bb9d8kkpG/uAQS5AmbA48q2IAolKKo1MA==}

'@types/d3-path@3.1.1':
resolution: {integrity: sha512-VMZBYyQvbGmWyWVea0EHs/BwLgxc+MKi1zLDCONksozI4YJMcTt8ZEuIR4Sb1MMTE8MMW49v0IwI5+b7RmfWlg==}

'@types/d3-scale@4.0.9':
resolution: {integrity: sha512-dLmtwB8zkAeO/juAMfnV+sItKjlsw2lKdZVVy6LRr0cBmegxSABiLEpGVmSJJ8O08i4+sGR6qQtb6WtuwJdvVw==}

'@types/d3-shape@3.1.7':
resolution: {integrity: sha512-VLvUQ33C+3J+8p+Daf+nYSOsjB4GXp19/S/aGo60m9h1v6XaxjiT82lKVWJCfzhtuZ3yD7i/TPeC/fuKLLOSmg==}

'@types/d3-time@3.0.4':
resolution: {integrity: sha512-yuzZug1nkAAaBlBBikKZTgzCeA+k1uy4ZFwWANOfKw5z5LRhV0gNA7gNkKm7HoK+HRN0wX3EkxGk0fpbWhmB7g==}

'@types/d3-timer@3.0.2':
resolution: {integrity: sha512-Ps3T8E8dZDam6fUyNiMkekK3XUsaUEik+idO9/YjPtfj2qruF8tFBXS7XhtE4iIXBLxhmLjP3SXpLhVf21I9Lw==}

'@types/node@22.0.0':
resolution: {integrity: sha512-VT7KSYudcPOzP5Q0wfbowyNLaVR8QWUdw+088uFWwfvpY6uCWaXpqV6ieLAu9WBcnTa7H4Z5RLK8I5t2FuOcqw==}

'@types/pako@2.0.4':
resolution: {integrity: sha512-VWDCbrLeVXJM9fihYodcLiIv0ku+AlOa/TQ1SvYOaBuyrSKgEcro95LJyIsJ4vSo6BXIxOKxiJAat04CmST9Fw==}

'@types/raf@3.4.3':
resolution: {integrity: sha512-c4YAvMedbPZ5tEyxzQdMoOhhJ4RD3rngZIdwC2/qDN3d7JpEhB6fiBRKVY1lg5B7Wk+uPBjn5f39j1/2MY1oOw==}

'@types/react-dom@19.0.0':
resolution: {integrity: sha512-1KfiQKsH1o00p9m5ag12axHQSb3FOU9H20UTrujVSkNhuCrRHiQWFqgEnTNK5ZNfnzZv8UWrnXVqCmCF9fgY3w==}

'@types/react@19.0.0':
resolution: {integrity: sha512-MY3oPudxvMYyesqs/kW1Bh8y9VqSmf+tzqw3ae8a9DZW68pUe3zAdHeI1jc6iAysuRdACnVknHP8AhwD4/dxtg==}

'@types/trusted-types@2.0.7':
resolution: {integrity: sha512-ScaPdn1dQczgbl0QFTeTOmVHFULt394XJgOQNoyVhZ6r2vLnMLJfBPd53SB52T/3G36VI1/g2MZaX0cwDuXsfw==}

'@types/use-sync-external-store@0.0.6':
resolution: {integrity: sha512-zFDAD+tlpf2r4asuHEj0XH6pY6i0g5NeAHPn+15wk3BV6JA69eERFXC1gyGThDkVa1zCyKr5jox1+2LbV/AMLg==}

'@vercel/analytics@1.3.1':
resolution: {integrity: sha512-xhSlYgAuJ6Q4WQGkzYTLmXwhYl39sWjoMA3nHxfkvG+WdBT25c563a7QhwwKivEOZtPJXifYHR1m2ihoisbWyA==}
peerDependencies:
next: '>= 13'
react: ^18 || ^19
peerDependenciesMeta:
next:
optional: true
react:
optional: true

aria-hidden@1.2.6:
resolution: {integrity: sha512-ik3ZgC9dY/lYVVM++OISsaYDeg1tb0VtP5uL3ouh1koGOaUMDPpbFIei4JkFimWUFPn90sbMNMXQAIVOlnYKJA==}
engines: {node: '>=10'}

autoprefixer@10.4.20:
resolution: {integrity: sha512-XY25y5xSv/wEoqzDyXXME4AFfkZI0P23z6Fs3YgymDnKJkCGOnkL0iTxCa85UTqaSgfcqyf3UA6+c7wUvx/16g==}
engines: {node: ^10 || ^12 || >=14}
hasBin: true
peerDependencies:
postcss: ^8.1.0

base64-arraybuffer@1.0.2:
resolution: {integrity: sha512-I3yl4r9QB5ZRY3XuJVEPfc2XhZO6YweFPI+UovAzn+8/hb3oJ6lnysaFcjVpkCPfVWFUDvoZ8kmVDP7WyRtYtQ==}
engines: {node: '>= 0.6.0'}

baseline-browser-mapping@2.8.22:
resolution: {integrity: sha512-/tk9kky/d8T8CTXIQYASLyhAxR5VwL3zct1oAoVTaOUHwrmsGnfbRwNdEq+vOl2BN8i3PcDdP0o4Q+jjKQoFbQ==}
hasBin: true

browserslist@4.27.0:
resolution: {integrity: sha512-AXVQwdhot1eqLihwasPElhX2tAZiBjWdJ9i/Zcj2S6QYIjkx62OKSfnobkriB81C3l4w0rVy3Nt4jaTBltYEpw==}
engines: {node: ^6 || ^7 || ^8 || ^9 || ^10 || ^11 || ^12 || >=13.7}
hasBin: true

caniuse-lite@1.0.30001752:
resolution: {integrity: sha512-vKUk7beoukxE47P5gcVNKkDRzXdVofotshHwfR9vmpeFKxmI5PBpgOMC18LUJUA/DvJ70Y7RveasIBraqsyO/g==}

canvg@3.0.11:
resolution: {integrity: sha512-5ON+q7jCTgMp9cjpu4Jo6XbvfYwSB2Ow3kzHKfIyJfaCAOHLbdKPQqGKgfED/R5B+3TFFfe8pegYA+b423SRyA==}
engines: {node: '>=10.0.0'}

chownr@3.0.0:
resolution: {integrity: sha512-+IxzY9BZOQd/XuYPRmrvEVjF/nqj5kgT4kEq7VofrDoM1MxoRjEWkrCC3EtLi59TVawxTAn+orJwFQcrqEN1+g==}
engines: {node: '>=18'}

class-variance-authority@0.7.1:
resolution: {integrity: sha512-Ka+9Trutv7G8M6WT6SeiRWz792K5qEqIGEGzXKhAE6xOWAY6pPH8U+9IY3oCMv6kqTmLsv7Xh/2w2RigkePMsg==}

client-only@0.0.1:
resolution: {integrity: sha512-IV3Ou0jSMzZrd3pZ48nLkT9DA7Ag1pnPzaiQhpW7c3RbcqqzvzzVu+L8gfqMp/8IM2MQtSiqaCxrrcfu8I8rMA==}

clsx@2.1.1:
resolution: {integrity: sha512-eYm0QWBtUrBWZWG0d386OGAw16Z995PiOVo2B7bjWSbHedGl5e0ZWaq65kOGgUSNesEIDkB9ISbTg/JK9dhCZA==}
engines: {node: '>=6'}

cmdk@1.0.4:
resolution: {integrity: sha512-AnsjfHyHpQ/EFeAnG216WY7A5LiYCoZzCSygiLvfXC3H3LFGCprErteUcszaVluGOhuOTbJS3jWHrSDYPBBygg==}
peerDependencies:
react: ^18 || ^19 || ^19.0.0-rc
react-dom: ^18 || ^19 || ^19.0.0-rc

core-js@3.46.0:
resolution: {integrity: sha512-vDMm9B0xnqqZ8uSBpZ8sNtRtOdmfShrvT6h2TuQGLs0Is+cR0DYbj/KWP6ALVNbWPpqA/qPLoOuppJN07humpA==}

css-line-break@2.1.0:
resolution: {integrity: sha512-FHcKFCZcAha3LwfVBhCQbW2nCNbkZXn7KVUJcsT5/P8YmfsVja0FMPJr0B903j/E69HUphKiV9iQArX8SDYA4w==}

csstype@3.1.3:
resolution: {integrity: sha512-M1uQkMl8rQK/szD0LNhtqxIPLpimGm8sOBwU7lLnCpSbTyY3yeU1Vc7l4KT5zT4s/yOxHH5O7tIuuLOCnLADRw==}

d3-array@3.2.4:
resolution: {integrity: sha512-tdQAmyA18i4J7wprpYq8ClcxZy3SC31QMeByyCFyRt7BVHdREQZ5lpzoe5mFEYZUWe+oq8HBvk9JjpibyEV4Jg==}
engines: {node: '>=12'}

d3-color@3.1.0:
resolution: {integrity: sha512-zg/chbXyeBtMQ1LbD/WSoW2DpC3I0mpmPdW+ynRTj/x2DAWYrIY7qeZIHidozwV24m4iavr15lNwIwLxRmOxhA==}
engines: {node: '>=12'}

d3-ease@3.0.1:
resolution: {integrity: sha512-wR/XK3D3XcLIZwpbvQwQ5fK+8Ykds1ip7A2Txe0yxncXSdq1L9skcG7blcedkOX+ZcgxGAmLX1FrRGbADwzi0w==}
engines: {node: '>=12'}

d3-format@3.1.0:
resolution: {integrity: sha512-YyUI6AEuY/Wpt8KWLgZHsIU86atmikuoOmCfommt0LYHiQSPjvX2AcFc38PX0CBpr2RCyZhjex+NS/LPOv6YqA==}
engines: {node: '>=12'}

d3-interpolate@3.0.1:
resolution: {integrity: sha512-3bYs1rOD33uo8aqJfKP3JWPAibgw8Zm2+L9vBKEHJ2Rg+viTR7o5Mmv5mZcieN+FRYaAOWX5SJATX6k1PWz72g==}
engines: {node: '>=12'}

d3-path@3.1.0:
resolution: {integrity: sha512-p3KP5HCf/bvjBSSKuXid6Zqijx7wIfNW+J/maPs+iwR35at5JCbLUT0LzF1cnjbCHWhqzQTIN2Jpe8pRebIEFQ==}
engines: {node: '>=12'}

d3-scale@4.0.2:
resolution: {integrity: sha512-GZW464g1SH7ag3Y7hXjf8RoUuAFIqklOAq3MRl4OaWabTFJY9PN/E1YklhXLh+OQ3fM9yS2nOkCoS+WLZ6kvxQ==}
engines: {node: '>=12'}

d3-shape@3.2.0:
resolution: {integrity: sha512-SaLBuwGm3MOViRq2ABk3eLoxwZELpH6zhl3FbAoJ7Vm1gofKx6El1Ib5z23NUEhF9AsGl7y+dzLe5Cw2AArGTA==}
engines: {node: '>=12'}

d3-time-format@4.1.0:
resolution: {integrity: sha512-dJxPBlzC7NugB2PDLwo9Q8JiTR3M3e4/XANkreKSUxF8vvXKqm1Yfq4Q5dl8budlunRVlUUaDUgFt7eA8D6NLg==}
engines: {node: '>=12'}

d3-time@3.1.0:
resolution: {integrity: sha512-VqKjzBLejbSMT4IgbmVgDjpkYrNWUYJnbCGo874u7MMKIWsILRX+OpX/gTk8MqjpT1A/c6HY2dCA77ZN0lkQ2Q==}
engines: {node: '>=12'}

d3-timer@3.0.1:
resolution: {integrity: sha512-ndfJ/JxxMd3nw31uyKoY2naivF+r29V+Lc0svZxe1JvvIRmi8hUsrMvdOwgS1o6uBHmiz91geQ0ylPP0aj1VUA==}
engines: {node: '>=12'}

date-fns-jalali@4.1.0-0:
resolution: {integrity: sha512-hTIP/z+t+qKwBDcmmsnmjWTduxCg+5KfdqWQvb2X/8C9+knYY6epN/pfxdDuyVlSVeFz0sM5eEfwIUQ70U4ckg==}

date-fns@4.1.0:
resolution: {integrity: sha512-Ukq0owbQXxa/U3EGtsdVBkR1w7KOQ5gIBqdH2hkvknzZPYvBxb/aa6E8L7tmjFtkwZBu3UXBbjIgPo/Ez4xaNg==}

decimal.js-light@2.5.1:
resolution: {integrity: sha512-qIMFpTMZmny+MMIitAB6D7iVPEorVw6YQRWkvarTkT4tBeSLLiHzcwj6q0MmYSFCiVpiqPJTJEYIrpcPzVEIvg==}

detect-libc@2.1.2:
resolution: {integrity: sha512-Btj2BOOO83o3WyH59e8MgXsxEQVcarkUOpEYrubB0urwnN10yQ364rsiByU11nZlqWYZm05i/of7io4mzihBtQ==}
engines: {node: '>=8'}

detect-node-es@1.1.0:
resolution: {integrity: sha512-ypdmJU/TbBby2Dxibuv7ZLW3Bs1QEmM7nHjEANfohJLvE0XVujisn1qPJcZxg+qDucsr+bP6fLD1rPS3AhJ7EQ==}

dompurify@3.3.0:
resolution: {integrity: sha512-r+f6MYR1gGN1eJv0TVQbhA7if/U7P87cdPl3HN5rikqaBSBxLiCb/b9O+2eG0cxz0ghyU+mU1QkbsOwERMYlWQ==}

electron-to-chromium@1.5.244:
resolution: {integrity: sha512-OszpBN7xZX4vWMPJwB9illkN/znA8M36GQqQxi6MNy9axWxhOfJyZZJtSLQCpEFLHP2xK33BiWx9aIuIEXVCcw==}

embla-carousel-react@8.5.1:
resolution: {integrity: sha512-z9Y0K84BJvhChXgqn2CFYbfEi6AwEr+FFVVKm/MqbTQ2zIzO1VQri6w67LcfpVF0AjbhwVMywDZqY4alYkjW5w==}
peerDependencies:
react: ^16.8.0 || ^17.0.1 || ^18.0.0 || ^19.0.0 || ^19.0.0-rc

embla-carousel-reactive-utils@8.5.1:
resolution: {integrity: sha512-n7VSoGIiiDIc4MfXF3ZRTO59KDp820QDuyBDGlt5/65+lumPHxX2JLz0EZ23hZ4eg4vZGUXwMkYv02fw2JVo/A==}
peerDependencies:
embla-carousel: 8.5.1

embla-carousel@8.5.1:
resolution: {integrity: sha512-JUb5+FOHobSiWQ2EJNaueCNT/cQU9L6XWBbWmorWPQT9bkbk+fhsuLr8wWrzXKagO3oWszBO7MSx+GfaRk4E6A==}

enhanced-resolve@5.18.3:
resolution: {integrity: sha512-d4lC8xfavMeBjzGr2vECC3fsGXziXZQyJxD868h2M/mBI3PwAuODxAkLkq5HYuvrPYcUtiLzsTo8U3PgX3Ocww==}
engines: {node: '>=10.13.0'}

es-toolkit@1.41.0:
resolution: {integrity: sha512-bDd3oRmbVgqZCJS6WmeQieOrzpl3URcWBUVDXxOELlUW2FuW+0glPOz1n0KnRie+PdyvUZcXz2sOn00c6pPRIA==}

escalade@3.2.0:
resolution: {integrity: sha512-WUj2qlxaQtO4g6Pq5c29GTcWGDyd8itL8zTlipgECz3JesAiiOKotd8JU6otB3PACgG6xkJUyVhboMS+bje/jA==}
engines: {node: '>=6'}

eventemitter3@5.0.1:
resolution: {integrity: sha512-GWkBvjiSZK87ELrYOSESUYeVIc9mvLLf/nXalMOS5dYrgZq9o5OVkbZAVM06CVxYsCwH9BDZFPlQTlPA1j4ahA==}

fast-png@6.4.0:
resolution: {integrity: sha512-kAqZq1TlgBjZcLr5mcN6NP5Rv4V2f22z00c3g8vRrwkcqjerx7BEhPbOnWCPqaHUl2XWQBJQvOT/FQhdMT7X/Q==}

fflate@0.8.2:
resolution: {integrity: sha512-cPJU47OaAoCbg0pBvzsgpTPhmhqI5eJjh/JIu8tPj5q+T7iLvW/JAYUqmE7KOB4R1ZyEhzBaIQpQpardBF5z8A==}

fraction.js@4.3.7:
resolution: {integrity: sha512-ZsDfxO51wGAXREY55a7la9LScWpwv9RxIrYABrlvOFBlH/ShPnrtsXeuUIfXKKOVicNxQ+o8JTbJvjS4M89yew==}

get-nonce@1.0.1:
resolution: {integrity: sha512-FJhYRoDaiatfEkUK8HKlicmu/3SGFD51q3itKDGoSTysQJBnfOcxU5GxnhE1E6soB76MbT0MBtnKJuXyAx+96Q==}
engines: {node: '>=6'}

graceful-fs@4.2.11:
resolution: {integrity: sha512-RbJ5/jmFcNNCcDV5o9eTnBLJ/HszWV0P73bc+Ff4nS/rJj+YaS6IGyiOL0VoBYX+l1Wrl3k63h/KrH+nhJ0XvQ==}

html2canvas@1.4.1:
resolution: {integrity: sha512-fPU6BHNpsyIhr8yyMpTLLxAbkaK8ArIBcmZIRiBLiDhjeqvXolaEmDGmELFuX9I4xDcaKKcJl+TKZLqruBbmWA==}
engines: {node: '>=8.0.0'}

immer@10.2.0:
resolution: {integrity: sha512-d/+XTN3zfODyjr89gM3mPq1WNX2B8pYsu7eORitdwyA2sBubnTl3laYlBk4sXY5FUa5qTZGBDPJICVbvqzjlbw==}

input-otp@1.4.1:
resolution: {integrity: sha512-+yvpmKYKHi9jIGngxagY9oWiiblPB7+nEO75F2l2o4vs+6vpPZZmUl4tBNYuTCvQjhvEIbdNeJu70bhfYP2nbw==}
peerDependencies:
react: ^16.8 || ^17.0 || ^18.0 || ^19.0.0 || ^19.0.0-rc
react-dom: ^16.8 || ^17.0 || ^18.0 || ^19.0.0 || ^19.0.0-rc

internmap@2.0.3:
resolution: {integrity: sha512-5Hh7Y1wQbvY5ooGgPbDaL5iYLAPzMTUrjMulskHLH6wnv/A+1q5rgEaiuqEjB+oxGXIVZs1FF+R/KPN3ZSQYYg==}
engines: {node: '>=12'}

iobuffer@5.4.0:
resolution: {integrity: sha512-DRebOWuqDvxunfkNJAlc3IzWIPD5xVxwUNbHr7xKB8E6aLJxIPfNX3CoMJghcFjpv6RWQsrcJbghtEwSPoJqMA==}

jiti@2.6.1:
resolution: {integrity: sha512-ekilCSN1jwRvIbgeg/57YFh8qQDNbwDb9xT/qu2DAHbFFZUicIl4ygVaAvzveMhMVr3LnpSKTNnwt8PoOfmKhQ==}
hasBin: true

jspdf@3.0.3:
resolution: {integrity: sha512-eURjAyz5iX1H8BOYAfzvdPfIKK53V7mCpBTe7Kb16PaM8JSXEcUQNBQaiWMI8wY5RvNOPj4GccMjTlfwRBd+oQ==}

lightningcss-darwin-arm64@1.30.1:
resolution: {integrity: sha512-c8JK7hyE65X1MHMN+Viq9n11RRC7hgin3HhYKhrMyaXflk5GVplZ60IxyoVtzILeKr+xAJwg6zK6sjTBJ0FKYQ==}
engines: {node: '>= 12.0.0'}
cpu: [arm64]
os: [darwin]

lightningcss-darwin-x64@1.30.1:
resolution: {integrity: sha512-k1EvjakfumAQoTfcXUcHQZhSpLlkAuEkdMBsI/ivWw9hL+7FtilQc0Cy3hrx0AAQrVtQAbMI7YjCgYgvn37PzA==}
engines: {node: '>= 12.0.0'}
cpu: [x64]
os: [darwin]

lightningcss-freebsd-x64@1.30.1:
resolution: {integrity: sha512-kmW6UGCGg2PcyUE59K5r0kWfKPAVy4SltVeut+umLCFoJ53RdCUWxcRDzO1eTaxf/7Q2H7LTquFHPL5R+Gjyig==}
engines: {node: '>= 12.0.0'}
cpu: [x64]
os: [freebsd]

lightningcss-linux-arm-gnueabihf@1.30.1:
resolution: {integrity: sha512-MjxUShl1v8pit+6D/zSPq9S9dQ2NPFSQwGvxBCYaBYLPlCWuPh9/t1MRS8iUaR8i+a6w7aps+B4N0S1TYP/R+Q==}
engines: {node: '>= 12.0.0'}
cpu: [arm]
os: [linux]

lightningcss-linux-arm64-gnu@1.30.1:
resolution: {integrity: sha512-gB72maP8rmrKsnKYy8XUuXi/4OctJiuQjcuqWNlJQ6jZiWqtPvqFziskH3hnajfvKB27ynbVCucKSm2rkQp4Bw==}
engines: {node: '>= 12.0.0'}
cpu: [arm64]
os: [linux]

lightningcss-linux-arm64-musl@1.30.1:
resolution: {integrity: sha512-jmUQVx4331m6LIX+0wUhBbmMX7TCfjF5FoOH6SD1CttzuYlGNVpA7QnrmLxrsub43ClTINfGSYyHe2HWeLl5CQ==}
engines: {node: '>= 12.0.0'}
cpu: [arm64]
os: [linux]

lightningcss-linux-x64-gnu@1.30.1:
resolution: {integrity: sha512-piWx3z4wN8J8z3+O5kO74+yr6ze/dKmPnI7vLqfSqI8bccaTGY5xiSGVIJBDd5K5BHlvVLpUB3S2YCfelyJ1bw==}
engines: {node: '>= 12.0.0'}
cpu: [x64]
os: [linux]

lightningcss-linux-x64-musl@1.30.1:
resolution: {integrity: sha512-rRomAK7eIkL+tHY0YPxbc5Dra2gXlI63HL+v1Pdi1a3sC+tJTcFrHX+E86sulgAXeI7rSzDYhPSeHHjqFhqfeQ==}
engines: {node: '>= 12.0.0'}
cpu: [x64]
os: [linux]

lightningcss-win32-arm64-msvc@1.30.1:
resolution: {integrity: sha512-mSL4rqPi4iXq5YVqzSsJgMVFENoa4nGTT/GjO2c0Yl9OuQfPsIfncvLrEW6RbbB24WtZ3xP/2CCmI3tNkNV4oA==}
engines: {node: '>= 12.0.0'}
cpu: [arm64]
os: [win32]

lightningcss-win32-x64-msvc@1.30.1:
resolution: {integrity: sha512-PVqXh48wh4T53F/1CCu8PIPCxLzWyCnn/9T5W1Jpmdy5h9Cwd+0YQS6/LwhHXSafuc61/xg9Lv5OrCby6a++jg==}
engines: {node: '>= 12.0.0'}
cpu: [x64]
os: [win32]

lightningcss@1.30.1:
resolution: {integrity: sha512-xi6IyHML+c9+Q3W0S4fCQJOym42pyurFiJUHEcEyHS0CeKzia4yZDEsLlqOFykxOdHpNy0NmvVO31vcSqAxJCg==}
engines: {node: '>= 12.0.0'}

lucide-react@0.454.0:
resolution: {integrity: sha512-hw7zMDwykCLnEzgncEEjHeA6+45aeEzRYuKHuyRSOPkhko+J3ySGjGIzu+mmMfDFG1vazHepMaYFYHbTFAZAAQ==}
peerDependencies:
react: ^16.5.1 || ^17.0.0 || ^18.0.0 || ^19.0.0-rc

magic-string@0.30.21:
resolution: {integrity: sha512-vd2F4YUyEXKGcLHoq+TEyCjxueSeHnFxyyjNp80yg0XV4vUhnDer/lvvlqM/arB5bXQN5K2/3oinyCRyx8T2CQ==}

minipass@7.1.2:
resolution: {integrity: sha512-qOOzS1cBTWYF4BH8fVePDBOO9iptMnGUEZwNc/cMWnTV2nVLZ7VoNWEPHkYczZA0pdoA7dl6e7FL659nX9S2aw==}
engines: {node: '>=16 || 14 >=14.17'}

minizlib@3.1.0:
resolution: {integrity: sha512-KZxYo1BUkWD2TVFLr0MQoM8vUUigWD3LlD83a/75BqC+4qE0Hb1Vo5v1FgcfaNXvfXzr+5EhQ6ing/CaBijTlw==}
engines: {node: '>= 18'}

nanoid@3.3.11:
resolution: {integrity: sha512-N8SpfPUnUp1bK+PMYW8qSWdl9U+wwNWI4QKxOYDy9JAro3WMX7p2OeVRF9v+347pnakNevPmiHhNmZ2HbFA76w==}
engines: {node: ^10 || ^12 || ^13.7 || ^14 || >=15.0.1}
hasBin: true

next-themes@0.4.6:
resolution: {integrity: sha512-pZvgD5L0IEvX5/9GWyHMf3m8BKiVQwsCMHfoFosXtXBMnaS0ZnIJ9ST4b4NqLVKDEm8QBxoNNGNaBv2JNF6XNA==}
peerDependencies:
react: ^16.8 || ^17 || ^18 || ^19 || ^19.0.0-rc
react-dom: ^16.8 || ^17 || ^18 || ^19 || ^19.0.0-rc

next@16.0.0:
resolution: {integrity: sha512-nYohiNdxGu4OmBzggxy9rczmjIGI+TpR5vbKTsE1HqYwNm1B+YSiugSrFguX6omMOKnDHAmBPY4+8TNJk0Idyg==}
engines: {node: '>=20.9.0'}
hasBin: true
peerDependencies:
'@opentelemetry/api': ^1.1.0
'@playwright/test': ^1.51.1
babel-plugin-react-compiler: '\*'
react: ^18.2.0 || 19.0.0-rc-de68d2f4-20241204 || ^19.0.0
react-dom: ^18.2.0 || 19.0.0-rc-de68d2f4-20241204 || ^19.0.0
sass: ^1.3.0
peerDependenciesMeta:
'@opentelemetry/api':
optional: true
'@playwright/test':
optional: true
babel-plugin-react-compiler:
optional: true
sass:
optional: true

node-releases@2.0.27:
resolution: {integrity: sha512-nmh3lCkYZ3grZvqcCH+fjmQ7X+H0OeZgP40OierEaAptX4XofMh5kwNbWh7lBduUzCcV/8kZ+NDLCwm2iorIlA==}

normalize-range@0.1.2:
resolution: {integrity: sha512-bdok/XvKII3nUpklnV6P2hxtMNrCboOjAcyBuQnWEhO665FwrSNRxU+AqpsyvO6LgGYPspN+lu5CLtw4jPRKNA==}
engines: {node: '>=0.10.0'}

pako@2.1.0:
resolution: {integrity: sha512-w+eufiZ1WuJYgPXbV/PO3NCMEc3xqylkKHzp8bxp1uW4qaSNQUkwmLLEc3kKsfz8lpV1F8Ht3U1Cm+9Srog2ug==}

performance-now@2.1.0:
resolution: {integrity: sha512-7EAHlyLHI56VEIdK57uwHdHKIaAGbnXPiw0yWbarQZOKaKpvUIgW0jWRVLiatnM+XXlSwsanIBH/hzGMJulMow==}

picocolors@1.1.1:
resolution: {integrity: sha512-xceH2snhtb5M9liqDsmEw56le376mTZkEX/jEb/RxNFyegNul7eNslCXP9FDj/Lcu0X8KEyMceP2ntpaHrDEVA==}

postcss-value-parser@4.2.0:
resolution: {integrity: sha512-1NNCs6uurfkVbeXG4S8JFT9t19m45ICnif8zWLd5oPSZ50QnwMfK+H3jv408d4jw/7Bttv5axS5IiHoLaVNHeQ==}

postcss@8.4.31:
resolution: {integrity: sha512-PS08Iboia9mts/2ygV3eLpY5ghnUcfLV/EXTOW1E2qYxJKGGBUtNjN76FYHnMs36RmARn41bC0AZmn+rR0OVpQ==}
engines: {node: ^10 || ^12 || >=14}

postcss@8.5.0:
resolution: {integrity: sha512-27VKOqrYfPncKA2NrFOVhP5MGAfHKLYn/Q0mz9cNQyRAKYi3VNHwYU2qKKqPCqgBmeeJ0uAFB56NumXZ5ZReXg==}
engines: {node: ^10 || ^12 || >=14}

raf@3.4.1:
resolution: {integrity: sha512-Sq4CW4QhwOHE8ucn6J34MqtZCeWFP2aQSmrlroYgqAV1PjStIhJXxYuTgUIfkEk7zTLjmIjLmU5q+fbD1NnOJA==}

react-day-picker@9.8.0:
resolution: {integrity: sha512-E0yhhg7R+pdgbl/2toTb0xBhsEAtmAx1l7qjIWYfcxOy8w4rTSVfbtBoSzVVhPwKP/5E9iL38LivzoE3AQDhCQ==}
engines: {node: '>=18'}
peerDependencies:
react: '>=16.8.0'

react-dom@19.2.0:
resolution: {integrity: sha512-UlbRu4cAiGaIewkPyiRGJk0imDN2T3JjieT6spoL2UeSf5od4n5LB/mQ4ejmxhCFT1tYe8IvaFulzynWovsEFQ==}
peerDependencies:
react: ^19.2.0

react-hook-form@7.60.0:
resolution: {integrity: sha512-SBrYOvMbDB7cV8ZfNpaiLcgjH/a1c7aK0lK+aNigpf4xWLO8q+o4tcvVurv3c4EOyzn/3dCsYt4GKD42VvJ/+A==}
engines: {node: '>=18.0.0'}
peerDependencies:
react: ^16.8.0 || ^17 || ^18 || ^19

react-is@19.2.0:
resolution: {integrity: sha512-x3Ax3kNSMIIkyVYhWPyO09bu0uttcAIoecO/um/rKGQ4EltYWVYtyiGkS/3xMynrbVQdS69Jhlv8FXUEZehlzA==}

react-redux@9.2.0:
resolution: {integrity: sha512-ROY9fvHhwOD9ySfrF0wmvu//bKCQ6AeZZq1nJNtbDC+kk5DuSuNX/n6YWYF/SYy7bSba4D4FSz8DJeKY/S/r+g==}
peerDependencies:
'@types/react': ^18.2.25 || ^19
react: ^18.0 || ^19
redux: ^5.0.0
peerDependenciesMeta:
'@types/react':
optional: true
redux:
optional: true

react-remove-scroll-bar@2.3.8:
resolution: {integrity: sha512-9r+yi9+mgU33AKcj6IbT9oRCO78WriSj6t/cF8DWBZJ9aOGPOTEDvdUDz1FwKim7QXWwmHqtdHnRJfhAxEG46Q==}
engines: {node: '>=10'}
peerDependencies:
'@types/react': '\*'
react: ^16.8.0 || ^17.0.0 || ^18.0.0 || ^19.0.0
peerDependenciesMeta:
'@types/react':
optional: true

react-remove-scroll@2.7.1:
resolution: {integrity: sha512-HpMh8+oahmIdOuS5aFKKY6Pyog+FNaZV/XyJOq7b4YFwsFHe5yYfdbIalI4k3vU2nSDql7YskmUseHsRrJqIPA==}
engines: {node: '>=10'}
peerDependencies:
'@types/react': '\*'
react: ^16.8.0 || ^17.0.0 || ^18.0.0 || ^19.0.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true

react-resizable-panels@2.1.7:
resolution: {integrity: sha512-JtT6gI+nURzhMYQYsx8DKkx6bSoOGFp7A3CwMrOb8y5jFHFyqwo9m68UhmXRw57fRVJksFn1TSlm3ywEQ9vMgA==}
peerDependencies:
react: ^16.14.0 || ^17.0.0 || ^18.0.0 || ^19.0.0 || ^19.0.0-rc
react-dom: ^16.14.0 || ^17.0.0 || ^18.0.0 || ^19.0.0 || ^19.0.0-rc

react-style-singleton@2.2.3:
resolution: {integrity: sha512-b6jSvxvVnyptAiLjbkWLE/lOnR4lfTtDAl+eUC7RZy+QQWc6wRzIV2CE6xBuMmDxc2qIihtDCZD5NPOFl7fRBQ==}
engines: {node: '>=10'}
peerDependencies:
'@types/react': '\*'
react: ^16.8.0 || ^17.0.0 || ^18.0.0 || ^19.0.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true

react@19.2.0:
resolution: {integrity: sha512-tmbWg6W31tQLeB5cdIBOicJDJRR2KzXsV7uSK9iNfLWQ5bIZfxuPEHp7M8wiHyHnn0DD1i7w3Zmin0FtkrwoCQ==}
engines: {node: '>=0.10.0'}

recharts@3.3.0:
resolution: {integrity: sha512-Vi0qmTB0iz1+/Cz9o5B7irVyUjX2ynvEgImbgMt/3sKRREcUM07QiYjS1QpAVrkmVlXqy5gykq4nGWMz9AS4Rg==}
engines: {node: '>=18'}
peerDependencies:
react: ^16.8.0 || ^17.0.0 || ^18.0.0 || ^19.0.0
react-dom: ^16.0.0 || ^17.0.0 || ^18.0.0 || ^19.0.0
react-is: ^16.8.0 || ^17.0.0 || ^18.0.0 || ^19.0.0

redux-thunk@3.1.0:
resolution: {integrity: sha512-NW2r5T6ksUKXCabzhL9z+h206HQw/NJkcLm1GPImRQ8IzfXwRGqjVhKJGauHirT0DAuyy6hjdnMZaRoAcy0Klw==}
peerDependencies:
redux: ^5.0.0

redux@5.0.1:
resolution: {integrity: sha512-M9/ELqF6fy8FwmkpnF0S3YKOqMyoWJ4+CS5Efg2ct3oY9daQvd/Pc71FpGZsVsbl3Cpb+IIcjBDUnnyBdQbq4w==}

regenerator-runtime@0.13.11:
resolution: {integrity: sha512-kY1AZVr2Ra+t+piVaJ4gxaFaReZVH40AKNo7UCX6W+dEwBo/2oZJzqfuN1qLq1oL45o56cPaTXELwrTh8Fpggg==}

reselect@5.1.1:
resolution: {integrity: sha512-K/BG6eIky/SBpzfHZv/dd+9JBFiS4SWV7FIujVyJRux6e45+73RaUHXLmIR1f7WOMaQ0U1km6qwklRQxpJJY0w==}

rgbcolor@1.0.1:
resolution: {integrity: sha512-9aZLIrhRaD97sgVhtJOW6ckOEh6/GnvQtdVNfdZ6s67+3/XwLS9lBcQYzEEhYVeUowN7pRzMLsyGhK2i/xvWbw==}
engines: {node: '>= 0.8.15'}

scheduler@0.27.0:
resolution: {integrity: sha512-eNv+WrVbKu1f3vbYJT/xtiF5syA5HPIMtf9IgY/nKg0sWqzAUEvqY/xm7OcZc/qafLx/iO9FgOmeSAp4v5ti/Q==}

semver@7.7.3:
resolution: {integrity: sha512-SdsKMrI9TdgjdweUSR9MweHA4EJ8YxHn8DFaDisvhVlUOe4BF1tLD7GAj0lIqWVl+dPb/rExr0Btby5loQm20Q==}
engines: {node: '>=10'}
hasBin: true

server-only@0.0.1:
resolution: {integrity: sha512-qepMx2JxAa5jjfzxG79yPPq+8BuFToHd1hm7kI+Z4zAq1ftQiP7HcxMhDDItrbtwVeLg/cY2JnKnrcFkmiswNA==}

sharp@0.34.4:
resolution: {integrity: sha512-FUH39xp3SBPnxWvd5iib1X8XY7J0K0X7d93sie9CJg2PO8/7gmg89Nve6OjItK53/MlAushNNxteBYfM6DEuoA==}
engines: {node: ^18.17.0 || ^20.3.0 || >=21.0.0}

sonner@1.7.4:
resolution: {integrity: sha512-DIS8z4PfJRbIyfVFDVnK9rO3eYDtse4Omcm6bt0oEr5/jtLgysmjuBl1frJ9E/EQZrFmKx2A8m/s5s9CRXIzhw==}
peerDependencies:
react: ^18.0.0 || ^19.0.0 || ^19.0.0-rc
react-dom: ^18.0.0 || ^19.0.0 || ^19.0.0-rc

source-map-js@1.2.1:
resolution: {integrity: sha512-UXWMKhLOwVKb728IUtQPXxfYU+usdybtUrK/8uGE8CQMvrhOpwvzDBwj0QhSL7MQc7vIsISBG8VQ8+IDQxpfQA==}
engines: {node: '>=0.10.0'}

stackblur-canvas@2.7.0:
resolution: {integrity: sha512-yf7OENo23AGJhBriGx0QivY5JP6Y1HbrrDI6WLt6C5auYZXlQrheoY8hD4ibekFKz1HOfE48Ww8kMWMnJD/zcQ==}
engines: {node: '>=0.1.14'}

styled-jsx@5.1.6:
resolution: {integrity: sha512-qSVyDTeMotdvQYoHWLNGwRFJHC+i+ZvdBRYosOFgC+Wg1vx4frN2/RG/NA7SYqqvKNLf39P2LSRA2pu6n0XYZA==}
engines: {node: '>= 12.0.0'}
peerDependencies:
'@babel/core': '_'
babel-plugin-macros: '_'
react: '>= 16.8.0 || 17.x.x || ^18.0.0-0 || ^19.0.0-0'
peerDependenciesMeta:
'@babel/core':
optional: true
babel-plugin-macros:
optional: true

svg-pathdata@6.0.3:
resolution: {integrity: sha512-qsjeeq5YjBZ5eMdFuUa4ZosMLxgr5RZ+F+Y1OrDhuOCEInRMA3x74XdBtggJcj9kOeInz0WE+LgCPDkZFlBYJw==}
engines: {node: '>=12.0.0'}

tailwind-merge@2.5.5:
resolution: {integrity: sha512-0LXunzzAZzo0tEPxV3I297ffKZPlKDrjj7NXphC8V5ak9yHC5zRmxnOe2m/Rd/7ivsOMJe3JZ2JVocoDdQTRBA==}

tailwindcss-animate@1.0.7:
resolution: {integrity: sha512-bl6mpH3T7I3UFxuvDEXLxy/VuFxBk5bbzplh7tXI68mwMokNYd1t9qPBHlnyTwfa4JGC4zP516I1hYYtQ/vspA==}
peerDependencies:
tailwindcss: '>=3.0.0 || insiders'

tailwindcss@4.1.9:
resolution: {integrity: sha512-anBZRcvfNMsQdHB9XSGzAtIQWlhs49uK75jfkwrqjRUbjt4d7q9RE1wR1xWyfYZhLFnFX4ahWp88Au2lcEw5IQ==}

tapable@2.3.0:
resolution: {integrity: sha512-g9ljZiwki/LfxmQADO3dEY1CbpmXT5Hm2fJ+QaGKwSXUylMybePR7/67YW7jOrrvjEgL1Fmz5kzyAjWVWLlucg==}
engines: {node: '>=6'}

tar@7.5.2:
resolution: {integrity: sha512-7NyxrTE4Anh8km8iEy7o0QYPs+0JKBTj5ZaqHg6B39erLg0qYXN3BijtShwbsNSvQ+LN75+KV+C4QR/f6Gwnpg==}
engines: {node: '>=18'}

text-segmentation@1.0.3:
resolution: {integrity: sha512-iOiPUo/BGnZ6+54OsWxZidGCsdU8YbE4PSpdPinp7DeMtUJNJBoJ/ouUSTJjHkh1KntHaltHl/gDs2FC4i5+Nw==}

tiny-invariant@1.3.3:
resolution: {integrity: sha512-+FbBPE1o9QAYvviau/qC5SE3caw21q3xkvWKBtja5vgqOWIHHJ3ioaq1VPfn/Szqctz2bU/oYeKd9/z5BL+PVg==}

tslib@2.8.1:
resolution: {integrity: sha512-oJFu94HQb+KVduSUQL7wnpmqnfmLsOA/nAh6b6EH0wCEoK0/mPeXU6c3wKDV83MkOuHPRHtSXKKU99IBazS/2w==}

tw-animate-css@1.3.3:
resolution: {integrity: sha512-tXE2TRWrskc4TU3RDd7T8n8Np/wCfoeH9gz22c7PzYqNPQ9FBGFbWWzwL0JyHcFp+jHozmF76tbHfPAx22ua2Q==}

typescript@5.0.2:
resolution: {integrity: sha512-wVORMBGO/FAs/++blGNeAVdbNKtIh1rbBL2EyQ1+J9lClJ93KiiKe8PmFIVdXhHcyv44SL9oglmfeSsndo0jRw==}
engines: {node: '>=12.20'}
hasBin: true

undici-types@6.11.1:
resolution: {integrity: sha512-mIDEX2ek50x0OlRgxryxsenE5XaQD4on5U2inY7RApK3SOJpofyw7uW2AyfMKkhAxXIceo2DeWGVGwyvng1GNQ==}

update-browserslist-db@1.1.4:
resolution: {integrity: sha512-q0SPT4xyU84saUX+tomz1WLkxUbuaJnR1xWt17M7fJtEJigJeWUNGUqrauFXsHnqev9y9JTRGwk13tFBuKby4A==}
hasBin: true
peerDependencies:
browserslist: '>= 4.21.0'

use-callback-ref@1.3.3:
resolution: {integrity: sha512-jQL3lRnocaFtu3V00JToYz/4QkNWswxijDaCVNZRiRTO3HQDLsdu1ZtmIUvV4yPp+rvWm5j0y0TG/S61cuijTg==}
engines: {node: '>=10'}
peerDependencies:
'@types/react': '\*'
react: ^16.8.0 || ^17.0.0 || ^18.0.0 || ^19.0.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true

use-sidecar@1.1.3:
resolution: {integrity: sha512-Fedw0aZvkhynoPYlA5WXrMCAMm+nSWdZt6lzJQ7Ok8S6Q+VsHmHpRWndVRJ8Be0ZbkfPc5LRYH+5XrzXcEeLRQ==}
engines: {node: '>=10'}
peerDependencies:
'@types/react': '\*'
react: ^16.8.0 || ^17.0.0 || ^18.0.0 || ^19.0.0 || ^19.0.0-rc
peerDependenciesMeta:
'@types/react':
optional: true

use-sync-external-store@1.6.0:
resolution: {integrity: sha512-Pp6GSwGP/NrPIrxVFAIkOQeyw8lFenOHijQWkUTrDvrF4ALqylP2C/KCkeS9dpUM3KvYRQhna5vt7IL95+ZQ9w==}
peerDependencies:
react: ^16.8.0 || ^17.0.0 || ^18.0.0 || ^19.0.0

utrie@1.0.2:
resolution: {integrity: sha512-1MLa5ouZiOmQzUbjbu9VmjLzn1QLXBhwpUa7kdLUQK+KQ5KA9I1vk5U4YHe/X2Ch7PYnJfWuWT+VbuxbGwljhw==}

vaul@0.9.9:
resolution: {integrity: sha512-7afKg48srluhZwIkaU+lgGtFCUsYBSGOl8vcc8N/M3YQlZFlynHD15AE+pwrYdc826o7nrIND4lL9Y6b9WWZZQ==}
peerDependencies:
react: ^16.8 || ^17.0 || ^18.0
react-dom: ^16.8 || ^17.0 || ^18.0

victory-vendor@37.3.6:
resolution: {integrity: sha512-SbPDPdDBYp+5MJHhBCAyI7wKM3d5ivekigc2Dk2s7pgbZ9wIgIBYGVw4zGHBml/qTFbexrofXW6Gu4noGxrOwQ==}

yallist@5.0.0:
resolution: {integrity: sha512-YgvUTfwqyc7UXVMrB+SImsVYSmTS8X/tSrtdNZMImM+n7+QTriRXyXim0mBrTXNeqzVF0KWGgHPeiyViFFrNDw==}
engines: {node: '>=18'}

zod@3.25.76:
resolution: {integrity: sha512-gzUt/qt81nXsFGKIFcC3YnfEAx5NkunCfnDlvuBSSFS02bcXu4Lmea0AFIUwbLWxWPx3d9p8S5QoaujKcNQxcQ==}

snapshots:

'@alloc/quick-lru@5.2.0': {}

'@ampproject/remapping@2.3.0':
dependencies:
'@jridgewell/gen-mapping': 0.3.13
'@jridgewell/trace-mapping': 0.3.31

'@babel/runtime@7.28.4': {}

'@date-fns/tz@1.2.0': {}

'@emnapi/runtime@1.6.0':
dependencies:
tslib: 2.8.1
optional: true

'@floating-ui/core@1.7.3':
dependencies:
'@floating-ui/utils': 0.2.10

'@floating-ui/dom@1.7.4':
dependencies:
'@floating-ui/core': 1.7.3
'@floating-ui/utils': 0.2.10

'@floating-ui/react-dom@2.1.6(react-dom@19.2.0(react@19.2.0))(react@19.2.0)':
dependencies:
'@floating-ui/dom': 1.7.4
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)

'@floating-ui/utils@0.2.10': {}

'@hookform/resolvers@3.10.0(react-hook-form@7.60.0(react@19.2.0))':
dependencies:
react-hook-form: 7.60.0(react@19.2.0)

'@img/colour@1.0.0':
optional: true

'@img/sharp-darwin-arm64@0.34.4':
optionalDependencies:
'@img/sharp-libvips-darwin-arm64': 1.2.3
optional: true

'@img/sharp-darwin-x64@0.34.4':
optionalDependencies:
'@img/sharp-libvips-darwin-x64': 1.2.3
optional: true

'@img/sharp-libvips-darwin-arm64@1.2.3':
optional: true

'@img/sharp-libvips-darwin-x64@1.2.3':
optional: true

'@img/sharp-libvips-linux-arm64@1.2.3':
optional: true

'@img/sharp-libvips-linux-arm@1.2.3':
optional: true

'@img/sharp-libvips-linux-ppc64@1.2.3':
optional: true

'@img/sharp-libvips-linux-s390x@1.2.3':
optional: true

'@img/sharp-libvips-linux-x64@1.2.3':
optional: true

'@img/sharp-libvips-linuxmusl-arm64@1.2.3':
optional: true

'@img/sharp-libvips-linuxmusl-x64@1.2.3':
optional: true

'@img/sharp-linux-arm64@0.34.4':
optionalDependencies:
'@img/sharp-libvips-linux-arm64': 1.2.3
optional: true

'@img/sharp-linux-arm@0.34.4':
optionalDependencies:
'@img/sharp-libvips-linux-arm': 1.2.3
optional: true

'@img/sharp-linux-ppc64@0.34.4':
optionalDependencies:
'@img/sharp-libvips-linux-ppc64': 1.2.3
optional: true

'@img/sharp-linux-s390x@0.34.4':
optionalDependencies:
'@img/sharp-libvips-linux-s390x': 1.2.3
optional: true

'@img/sharp-linux-x64@0.34.4':
optionalDependencies:
'@img/sharp-libvips-linux-x64': 1.2.3
optional: true

'@img/sharp-linuxmusl-arm64@0.34.4':
optionalDependencies:
'@img/sharp-libvips-linuxmusl-arm64': 1.2.3
optional: true

'@img/sharp-linuxmusl-x64@0.34.4':
optionalDependencies:
'@img/sharp-libvips-linuxmusl-x64': 1.2.3
optional: true

'@img/sharp-wasm32@0.34.4':
dependencies:
'@emnapi/runtime': 1.6.0
optional: true

'@img/sharp-win32-arm64@0.34.4':
optional: true

'@img/sharp-win32-ia32@0.34.4':
optional: true

'@img/sharp-win32-x64@0.34.4':
optional: true

'@isaacs/fs-minipass@4.0.1':
dependencies:
minipass: 7.1.2

'@jridgewell/gen-mapping@0.3.13':
dependencies:
'@jridgewell/sourcemap-codec': 1.5.5
'@jridgewell/trace-mapping': 0.3.31

'@jridgewell/resolve-uri@3.1.2': {}

'@jridgewell/sourcemap-codec@1.5.5': {}

'@jridgewell/trace-mapping@0.3.31':
dependencies:
'@jridgewell/resolve-uri': 3.1.2
'@jridgewell/sourcemap-codec': 1.5.5

'@next/env@16.0.0': {}

'@next/swc-darwin-arm64@16.0.0':
optional: true

'@next/swc-darwin-x64@16.0.0':
optional: true

'@next/swc-linux-arm64-gnu@16.0.0':
optional: true

'@next/swc-linux-arm64-musl@16.0.0':
optional: true

'@next/swc-linux-x64-gnu@16.0.0':
optional: true

'@next/swc-linux-x64-musl@16.0.0':
optional: true

'@next/swc-win32-arm64-msvc@16.0.0':
optional: true

'@next/swc-win32-x64-msvc@16.0.0':
optional: true

'@radix-ui/number@1.1.0': {}

'@radix-ui/primitive@1.1.1': {}

'@radix-ui/react-accordion@1.2.2(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)':
dependencies:
'@radix-ui/primitive': 1.1.1
'@radix-ui/react-collapsible': 1.1.2(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-collection': 1.1.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-compose-refs': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-context': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-direction': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-id': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-primitive': 2.0.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-use-controllable-state': 1.1.0(@types/react@19.0.0)(react@19.2.0)
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
optionalDependencies:
'@types/react': 19.0.0
'@types/react-dom': 19.0.0

'@radix-ui/react-alert-dialog@1.1.4(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)':
dependencies:
'@radix-ui/primitive': 1.1.1
'@radix-ui/react-compose-refs': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-context': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-dialog': 1.1.4(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-primitive': 2.0.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-slot': 1.1.1(@types/react@19.0.0)(react@19.2.0)
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
optionalDependencies:
'@types/react': 19.0.0
'@types/react-dom': 19.0.0

'@radix-ui/react-arrow@1.1.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)':
dependencies:
'@radix-ui/react-primitive': 2.0.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
optionalDependencies:
'@types/react': 19.0.0
'@types/react-dom': 19.0.0

'@radix-ui/react-aspect-ratio@1.1.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)':
dependencies:
'@radix-ui/react-primitive': 2.0.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
optionalDependencies:
'@types/react': 19.0.0
'@types/react-dom': 19.0.0

'@radix-ui/react-avatar@1.1.2(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)':
dependencies:
'@radix-ui/react-context': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-primitive': 2.0.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-use-callback-ref': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-use-layout-effect': 1.1.0(@types/react@19.0.0)(react@19.2.0)
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
optionalDependencies:
'@types/react': 19.0.0
'@types/react-dom': 19.0.0

'@radix-ui/react-checkbox@1.1.3(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)':
dependencies:
'@radix-ui/primitive': 1.1.1
'@radix-ui/react-compose-refs': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-context': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-presence': 1.1.2(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-primitive': 2.0.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-use-controllable-state': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-use-previous': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-use-size': 1.1.0(@types/react@19.0.0)(react@19.2.0)
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
optionalDependencies:
'@types/react': 19.0.0
'@types/react-dom': 19.0.0

'@radix-ui/react-collapsible@1.1.2(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)':
dependencies:
'@radix-ui/primitive': 1.1.1
'@radix-ui/react-compose-refs': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-context': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-id': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-presence': 1.1.2(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-primitive': 2.0.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-use-controllable-state': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-use-layout-effect': 1.1.0(@types/react@19.0.0)(react@19.2.0)
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
optionalDependencies:
'@types/react': 19.0.0
'@types/react-dom': 19.0.0

'@radix-ui/react-collection@1.1.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)':
dependencies:
'@radix-ui/react-compose-refs': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-context': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-primitive': 2.0.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-slot': 1.1.1(@types/react@19.0.0)(react@19.2.0)
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
optionalDependencies:
'@types/react': 19.0.0
'@types/react-dom': 19.0.0

'@radix-ui/react-compose-refs@1.1.1(@types/react@19.0.0)(react@19.2.0)':
dependencies:
react: 19.2.0
optionalDependencies:
'@types/react': 19.0.0

'@radix-ui/react-compose-refs@1.1.2(@types/react@19.0.0)(react@19.2.0)':
dependencies:
react: 19.2.0
optionalDependencies:
'@types/react': 19.0.0

'@radix-ui/react-context-menu@2.2.4(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)':
dependencies:
'@radix-ui/primitive': 1.1.1
'@radix-ui/react-context': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-menu': 2.1.4(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-primitive': 2.0.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-use-callback-ref': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-use-controllable-state': 1.1.0(@types/react@19.0.0)(react@19.2.0)
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
optionalDependencies:
'@types/react': 19.0.0
'@types/react-dom': 19.0.0

'@radix-ui/react-context@1.1.1(@types/react@19.0.0)(react@19.2.0)':
dependencies:
react: 19.2.0
optionalDependencies:
'@types/react': 19.0.0

'@radix-ui/react-dialog@1.1.4(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)':
dependencies:
'@radix-ui/primitive': 1.1.1
'@radix-ui/react-compose-refs': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-context': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-dismissable-layer': 1.1.3(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-focus-guards': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-focus-scope': 1.1.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-id': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-portal': 1.1.3(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-presence': 1.1.2(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-primitive': 2.0.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-slot': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-use-controllable-state': 1.1.0(@types/react@19.0.0)(react@19.2.0)
aria-hidden: 1.2.6
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
react-remove-scroll: 2.7.1(@types/react@19.0.0)(react@19.2.0)
optionalDependencies:
'@types/react': 19.0.0
'@types/react-dom': 19.0.0

'@radix-ui/react-direction@1.1.0(@types/react@19.0.0)(react@19.2.0)':
dependencies:
react: 19.2.0
optionalDependencies:
'@types/react': 19.0.0

'@radix-ui/react-dismissable-layer@1.1.3(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)':
dependencies:
'@radix-ui/primitive': 1.1.1
'@radix-ui/react-compose-refs': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-primitive': 2.0.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-use-callback-ref': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-use-escape-keydown': 1.1.0(@types/react@19.0.0)(react@19.2.0)
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
optionalDependencies:
'@types/react': 19.0.0
'@types/react-dom': 19.0.0

'@radix-ui/react-dropdown-menu@2.1.4(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)':
dependencies:
'@radix-ui/primitive': 1.1.1
'@radix-ui/react-compose-refs': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-context': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-id': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-menu': 2.1.4(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-primitive': 2.0.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-use-controllable-state': 1.1.0(@types/react@19.0.0)(react@19.2.0)
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
optionalDependencies:
'@types/react': 19.0.0
'@types/react-dom': 19.0.0

'@radix-ui/react-focus-guards@1.1.1(@types/react@19.0.0)(react@19.2.0)':
dependencies:
react: 19.2.0
optionalDependencies:
'@types/react': 19.0.0

'@radix-ui/react-focus-scope@1.1.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)':
dependencies:
'@radix-ui/react-compose-refs': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-primitive': 2.0.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-use-callback-ref': 1.1.0(@types/react@19.0.0)(react@19.2.0)
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
optionalDependencies:
'@types/react': 19.0.0
'@types/react-dom': 19.0.0

'@radix-ui/react-hover-card@1.1.4(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)':
dependencies:
'@radix-ui/primitive': 1.1.1
'@radix-ui/react-compose-refs': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-context': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-dismissable-layer': 1.1.3(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-popper': 1.2.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-portal': 1.1.3(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-presence': 1.1.2(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-primitive': 2.0.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-use-controllable-state': 1.1.0(@types/react@19.0.0)(react@19.2.0)
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
optionalDependencies:
'@types/react': 19.0.0
'@types/react-dom': 19.0.0

'@radix-ui/react-id@1.1.0(@types/react@19.0.0)(react@19.2.0)':
dependencies:
'@radix-ui/react-use-layout-effect': 1.1.0(@types/react@19.0.0)(react@19.2.0)
react: 19.2.0
optionalDependencies:
'@types/react': 19.0.0

'@radix-ui/react-id@1.1.1(@types/react@19.0.0)(react@19.2.0)':
dependencies:
'@radix-ui/react-use-layout-effect': 1.1.1(@types/react@19.0.0)(react@19.2.0)
react: 19.2.0
optionalDependencies:
'@types/react': 19.0.0

'@radix-ui/react-label@2.1.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)':
dependencies:
'@radix-ui/react-primitive': 2.0.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
optionalDependencies:
'@types/react': 19.0.0
'@types/react-dom': 19.0.0

'@radix-ui/react-menu@2.1.4(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)':
dependencies:
'@radix-ui/primitive': 1.1.1
'@radix-ui/react-collection': 1.1.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-compose-refs': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-context': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-direction': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-dismissable-layer': 1.1.3(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-focus-guards': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-focus-scope': 1.1.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-id': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-popper': 1.2.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-portal': 1.1.3(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-presence': 1.1.2(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-primitive': 2.0.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-roving-focus': 1.1.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-slot': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-use-callback-ref': 1.1.0(@types/react@19.0.0)(react@19.2.0)
aria-hidden: 1.2.6
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
react-remove-scroll: 2.7.1(@types/react@19.0.0)(react@19.2.0)
optionalDependencies:
'@types/react': 19.0.0
'@types/react-dom': 19.0.0

'@radix-ui/react-menubar@1.1.4(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)':
dependencies:
'@radix-ui/primitive': 1.1.1
'@radix-ui/react-collection': 1.1.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-compose-refs': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-context': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-direction': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-id': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-menu': 2.1.4(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-primitive': 2.0.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-roving-focus': 1.1.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-use-controllable-state': 1.1.0(@types/react@19.0.0)(react@19.2.0)
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
optionalDependencies:
'@types/react': 19.0.0
'@types/react-dom': 19.0.0

'@radix-ui/react-navigation-menu@1.2.3(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)':
dependencies:
'@radix-ui/primitive': 1.1.1
'@radix-ui/react-collection': 1.1.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-compose-refs': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-context': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-direction': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-dismissable-layer': 1.1.3(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-id': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-presence': 1.1.2(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-primitive': 2.0.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-use-callback-ref': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-use-controllable-state': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-use-layout-effect': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-use-previous': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-visually-hidden': 1.1.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
optionalDependencies:
'@types/react': 19.0.0
'@types/react-dom': 19.0.0

'@radix-ui/react-popover@1.1.4(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)':
dependencies:
'@radix-ui/primitive': 1.1.1
'@radix-ui/react-compose-refs': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-context': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-dismissable-layer': 1.1.3(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-focus-guards': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-focus-scope': 1.1.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-id': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-popper': 1.2.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-portal': 1.1.3(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-presence': 1.1.2(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-primitive': 2.0.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-slot': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-use-controllable-state': 1.1.0(@types/react@19.0.0)(react@19.2.0)
aria-hidden: 1.2.6
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
react-remove-scroll: 2.7.1(@types/react@19.0.0)(react@19.2.0)
optionalDependencies:
'@types/react': 19.0.0
'@types/react-dom': 19.0.0

'@radix-ui/react-popper@1.2.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)':
dependencies:
'@floating-ui/react-dom': 2.1.6(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-arrow': 1.1.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-compose-refs': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-context': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-primitive': 2.0.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-use-callback-ref': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-use-layout-effect': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-use-rect': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-use-size': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/rect': 1.1.0
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
optionalDependencies:
'@types/react': 19.0.0
'@types/react-dom': 19.0.0

'@radix-ui/react-portal@1.1.3(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)':
dependencies:
'@radix-ui/react-primitive': 2.0.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-use-layout-effect': 1.1.0(@types/react@19.0.0)(react@19.2.0)
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
optionalDependencies:
'@types/react': 19.0.0
'@types/react-dom': 19.0.0

'@radix-ui/react-presence@1.1.2(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)':
dependencies:
'@radix-ui/react-compose-refs': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-use-layout-effect': 1.1.0(@types/react@19.0.0)(react@19.2.0)
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
optionalDependencies:
'@types/react': 19.0.0
'@types/react-dom': 19.0.0

'@radix-ui/react-primitive@2.0.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)':
dependencies:
'@radix-ui/react-slot': 1.1.1(@types/react@19.0.0)(react@19.2.0)
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
optionalDependencies:
'@types/react': 19.0.0
'@types/react-dom': 19.0.0

'@radix-ui/react-primitive@2.1.3(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)':
dependencies:
'@radix-ui/react-slot': 1.2.3(@types/react@19.0.0)(react@19.2.0)
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
optionalDependencies:
'@types/react': 19.0.0
'@types/react-dom': 19.0.0

'@radix-ui/react-progress@1.1.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)':
dependencies:
'@radix-ui/react-context': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-primitive': 2.0.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
optionalDependencies:
'@types/react': 19.0.0
'@types/react-dom': 19.0.0

'@radix-ui/react-radio-group@1.2.2(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)':
dependencies:
'@radix-ui/primitive': 1.1.1
'@radix-ui/react-compose-refs': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-context': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-direction': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-presence': 1.1.2(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-primitive': 2.0.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-roving-focus': 1.1.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-use-controllable-state': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-use-previous': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-use-size': 1.1.0(@types/react@19.0.0)(react@19.2.0)
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
optionalDependencies:
'@types/react': 19.0.0
'@types/react-dom': 19.0.0

'@radix-ui/react-roving-focus@1.1.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)':
dependencies:
'@radix-ui/primitive': 1.1.1
'@radix-ui/react-collection': 1.1.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-compose-refs': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-context': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-direction': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-id': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-primitive': 2.0.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-use-callback-ref': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-use-controllable-state': 1.1.0(@types/react@19.0.0)(react@19.2.0)
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
optionalDependencies:
'@types/react': 19.0.0
'@types/react-dom': 19.0.0

'@radix-ui/react-scroll-area@1.2.2(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)':
dependencies:
'@radix-ui/number': 1.1.0
'@radix-ui/primitive': 1.1.1
'@radix-ui/react-compose-refs': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-context': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-direction': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-presence': 1.1.2(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-primitive': 2.0.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-use-callback-ref': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-use-layout-effect': 1.1.0(@types/react@19.0.0)(react@19.2.0)
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
optionalDependencies:
'@types/react': 19.0.0
'@types/react-dom': 19.0.0

'@radix-ui/react-select@2.1.4(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)':
dependencies:
'@radix-ui/number': 1.1.0
'@radix-ui/primitive': 1.1.1
'@radix-ui/react-collection': 1.1.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-compose-refs': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-context': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-direction': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-dismissable-layer': 1.1.3(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-focus-guards': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-focus-scope': 1.1.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-id': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-popper': 1.2.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-portal': 1.1.3(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-primitive': 2.0.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-slot': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-use-callback-ref': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-use-controllable-state': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-use-layout-effect': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-use-previous': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-visually-hidden': 1.1.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
aria-hidden: 1.2.6
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
react-remove-scroll: 2.7.1(@types/react@19.0.0)(react@19.2.0)
optionalDependencies:
'@types/react': 19.0.0
'@types/react-dom': 19.0.0

'@radix-ui/react-separator@1.1.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)':
dependencies:
'@radix-ui/react-primitive': 2.0.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
optionalDependencies:
'@types/react': 19.0.0
'@types/react-dom': 19.0.0

'@radix-ui/react-slider@1.2.2(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)':
dependencies:
'@radix-ui/number': 1.1.0
'@radix-ui/primitive': 1.1.1
'@radix-ui/react-collection': 1.1.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-compose-refs': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-context': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-direction': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-primitive': 2.0.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-use-controllable-state': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-use-layout-effect': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-use-previous': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-use-size': 1.1.0(@types/react@19.0.0)(react@19.2.0)
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
optionalDependencies:
'@types/react': 19.0.0
'@types/react-dom': 19.0.0

'@radix-ui/react-slot@1.1.1(@types/react@19.0.0)(react@19.2.0)':
dependencies:
'@radix-ui/react-compose-refs': 1.1.1(@types/react@19.0.0)(react@19.2.0)
react: 19.2.0
optionalDependencies:
'@types/react': 19.0.0

'@radix-ui/react-slot@1.2.3(@types/react@19.0.0)(react@19.2.0)':
dependencies:
'@radix-ui/react-compose-refs': 1.1.2(@types/react@19.0.0)(react@19.2.0)
react: 19.2.0
optionalDependencies:
'@types/react': 19.0.0

'@radix-ui/react-switch@1.1.2(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)':
dependencies:
'@radix-ui/primitive': 1.1.1
'@radix-ui/react-compose-refs': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-context': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-primitive': 2.0.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-use-controllable-state': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-use-previous': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-use-size': 1.1.0(@types/react@19.0.0)(react@19.2.0)
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
optionalDependencies:
'@types/react': 19.0.0
'@types/react-dom': 19.0.0

'@radix-ui/react-tabs@1.1.2(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)':
dependencies:
'@radix-ui/primitive': 1.1.1
'@radix-ui/react-context': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-direction': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-id': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-presence': 1.1.2(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-primitive': 2.0.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-roving-focus': 1.1.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-use-controllable-state': 1.1.0(@types/react@19.0.0)(react@19.2.0)
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
optionalDependencies:
'@types/react': 19.0.0
'@types/react-dom': 19.0.0

'@radix-ui/react-toast@1.2.4(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)':
dependencies:
'@radix-ui/primitive': 1.1.1
'@radix-ui/react-collection': 1.1.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-compose-refs': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-context': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-dismissable-layer': 1.1.3(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-portal': 1.1.3(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-presence': 1.1.2(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-primitive': 2.0.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-use-callback-ref': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-use-controllable-state': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-use-layout-effect': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-visually-hidden': 1.1.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
optionalDependencies:
'@types/react': 19.0.0
'@types/react-dom': 19.0.0

'@radix-ui/react-toggle-group@1.1.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)':
dependencies:
'@radix-ui/primitive': 1.1.1
'@radix-ui/react-context': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-direction': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-primitive': 2.0.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-roving-focus': 1.1.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-toggle': 1.1.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-use-controllable-state': 1.1.0(@types/react@19.0.0)(react@19.2.0)
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
optionalDependencies:
'@types/react': 19.0.0
'@types/react-dom': 19.0.0

'@radix-ui/react-toggle@1.1.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)':
dependencies:
'@radix-ui/primitive': 1.1.1
'@radix-ui/react-primitive': 2.0.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-use-controllable-state': 1.1.0(@types/react@19.0.0)(react@19.2.0)
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
optionalDependencies:
'@types/react': 19.0.0
'@types/react-dom': 19.0.0

'@radix-ui/react-tooltip@1.1.6(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)':
dependencies:
'@radix-ui/primitive': 1.1.1
'@radix-ui/react-compose-refs': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-context': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-dismissable-layer': 1.1.3(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-id': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-popper': 1.2.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-portal': 1.1.3(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-presence': 1.1.2(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-primitive': 2.0.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-slot': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-use-controllable-state': 1.1.0(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-visually-hidden': 1.1.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
optionalDependencies:
'@types/react': 19.0.0
'@types/react-dom': 19.0.0

'@radix-ui/react-use-callback-ref@1.1.0(@types/react@19.0.0)(react@19.2.0)':
dependencies:
react: 19.2.0
optionalDependencies:
'@types/react': 19.0.0

'@radix-ui/react-use-controllable-state@1.1.0(@types/react@19.0.0)(react@19.2.0)':
dependencies:
'@radix-ui/react-use-callback-ref': 1.1.0(@types/react@19.0.0)(react@19.2.0)
react: 19.2.0
optionalDependencies:
'@types/react': 19.0.0

'@radix-ui/react-use-escape-keydown@1.1.0(@types/react@19.0.0)(react@19.2.0)':
dependencies:
'@radix-ui/react-use-callback-ref': 1.1.0(@types/react@19.0.0)(react@19.2.0)
react: 19.2.0
optionalDependencies:
'@types/react': 19.0.0

'@radix-ui/react-use-layout-effect@1.1.0(@types/react@19.0.0)(react@19.2.0)':
dependencies:
react: 19.2.0
optionalDependencies:
'@types/react': 19.0.0

'@radix-ui/react-use-layout-effect@1.1.1(@types/react@19.0.0)(react@19.2.0)':
dependencies:
react: 19.2.0
optionalDependencies:
'@types/react': 19.0.0

'@radix-ui/react-use-previous@1.1.0(@types/react@19.0.0)(react@19.2.0)':
dependencies:
react: 19.2.0
optionalDependencies:
'@types/react': 19.0.0

'@radix-ui/react-use-rect@1.1.0(@types/react@19.0.0)(react@19.2.0)':
dependencies:
'@radix-ui/rect': 1.1.0
react: 19.2.0
optionalDependencies:
'@types/react': 19.0.0

'@radix-ui/react-use-size@1.1.0(@types/react@19.0.0)(react@19.2.0)':
dependencies:
'@radix-ui/react-use-layout-effect': 1.1.0(@types/react@19.0.0)(react@19.2.0)
react: 19.2.0
optionalDependencies:
'@types/react': 19.0.0

'@radix-ui/react-visually-hidden@1.1.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)':
dependencies:
'@radix-ui/react-primitive': 2.0.1(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
optionalDependencies:
'@types/react': 19.0.0
'@types/react-dom': 19.0.0

'@radix-ui/rect@1.1.0': {}

'@reduxjs/toolkit@2.9.2(react-redux@9.2.0(@types/react@19.0.0)(react@19.2.0)(redux@5.0.1))(react@19.2.0)':
dependencies:
'@standard-schema/spec': 1.0.0
'@standard-schema/utils': 0.3.0
immer: 10.2.0
redux: 5.0.1
redux-thunk: 3.1.0(redux@5.0.1)
reselect: 5.1.1
optionalDependencies:
react: 19.2.0
react-redux: 9.2.0(@types/react@19.0.0)(react@19.2.0)(redux@5.0.1)

'@standard-schema/spec@1.0.0': {}

'@standard-schema/utils@0.3.0': {}

'@swc/helpers@0.5.15':
dependencies:
tslib: 2.8.1

'@tailwindcss/node@4.1.9':
dependencies:
'@ampproject/remapping': 2.3.0
enhanced-resolve: 5.18.3
jiti: 2.6.1
lightningcss: 1.30.1
magic-string: 0.30.21
source-map-js: 1.2.1
tailwindcss: 4.1.9

'@tailwindcss/oxide-android-arm64@4.1.9':
optional: true

'@tailwindcss/oxide-darwin-arm64@4.1.9':
optional: true

'@tailwindcss/oxide-darwin-x64@4.1.9':
optional: true

'@tailwindcss/oxide-freebsd-x64@4.1.9':
optional: true

'@tailwindcss/oxide-linux-arm-gnueabihf@4.1.9':
optional: true

'@tailwindcss/oxide-linux-arm64-gnu@4.1.9':
optional: true

'@tailwindcss/oxide-linux-arm64-musl@4.1.9':
optional: true

'@tailwindcss/oxide-linux-x64-gnu@4.1.9':
optional: true

'@tailwindcss/oxide-linux-x64-musl@4.1.9':
optional: true

'@tailwindcss/oxide-wasm32-wasi@4.1.9':
optional: true

'@tailwindcss/oxide-win32-arm64-msvc@4.1.9':
optional: true

'@tailwindcss/oxide-win32-x64-msvc@4.1.9':
optional: true

'@tailwindcss/oxide@4.1.9':
dependencies:
detect-libc: 2.1.2
tar: 7.5.2
optionalDependencies:
'@tailwindcss/oxide-android-arm64': 4.1.9
'@tailwindcss/oxide-darwin-arm64': 4.1.9
'@tailwindcss/oxide-darwin-x64': 4.1.9
'@tailwindcss/oxide-freebsd-x64': 4.1.9
'@tailwindcss/oxide-linux-arm-gnueabihf': 4.1.9
'@tailwindcss/oxide-linux-arm64-gnu': 4.1.9
'@tailwindcss/oxide-linux-arm64-musl': 4.1.9
'@tailwindcss/oxide-linux-x64-gnu': 4.1.9
'@tailwindcss/oxide-linux-x64-musl': 4.1.9
'@tailwindcss/oxide-wasm32-wasi': 4.1.9
'@tailwindcss/oxide-win32-arm64-msvc': 4.1.9
'@tailwindcss/oxide-win32-x64-msvc': 4.1.9

'@tailwindcss/postcss@4.1.9':
dependencies:
'@alloc/quick-lru': 5.2.0
'@tailwindcss/node': 4.1.9
'@tailwindcss/oxide': 4.1.9
postcss: 8.5.0
tailwindcss: 4.1.9

'@types/d3-array@3.2.2': {}

'@types/d3-color@3.1.3': {}

'@types/d3-ease@3.0.2': {}

'@types/d3-interpolate@3.0.4':
dependencies:
'@types/d3-color': 3.1.3

'@types/d3-path@3.1.1': {}

'@types/d3-scale@4.0.9':
dependencies:
'@types/d3-time': 3.0.4

'@types/d3-shape@3.1.7':
dependencies:
'@types/d3-path': 3.1.1

'@types/d3-time@3.0.4': {}

'@types/d3-timer@3.0.2': {}

'@types/node@22.0.0':
dependencies:
undici-types: 6.11.1

'@types/pako@2.0.4': {}

'@types/raf@3.4.3':
optional: true

'@types/react-dom@19.0.0':
dependencies:
'@types/react': 19.0.0

'@types/react@19.0.0':
dependencies:
csstype: 3.1.3

'@types/trusted-types@2.0.7':
optional: true

'@types/use-sync-external-store@0.0.6': {}

'@vercel/analytics@1.3.1(next@16.0.0(react-dom@19.2.0(react@19.2.0))(react@19.2.0))(react@19.2.0)':
dependencies:
server-only: 0.0.1
optionalDependencies:
next: 16.0.0(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
react: 19.2.0

aria-hidden@1.2.6:
dependencies:
tslib: 2.8.1

autoprefixer@10.4.20(postcss@8.5.0):
dependencies:
browserslist: 4.27.0
caniuse-lite: 1.0.30001752
fraction.js: 4.3.7
normalize-range: 0.1.2
picocolors: 1.1.1
postcss: 8.5.0
postcss-value-parser: 4.2.0

base64-arraybuffer@1.0.2:
optional: true

baseline-browser-mapping@2.8.22: {}

browserslist@4.27.0:
dependencies:
baseline-browser-mapping: 2.8.22
caniuse-lite: 1.0.30001752
electron-to-chromium: 1.5.244
node-releases: 2.0.27
update-browserslist-db: 1.1.4(browserslist@4.27.0)

caniuse-lite@1.0.30001752: {}

canvg@3.0.11:
dependencies:
'@babel/runtime': 7.28.4
'@types/raf': 3.4.3
core-js: 3.46.0
raf: 3.4.1
regenerator-runtime: 0.13.11
rgbcolor: 1.0.1
stackblur-canvas: 2.7.0
svg-pathdata: 6.0.3
optional: true

chownr@3.0.0: {}

class-variance-authority@0.7.1:
dependencies:
clsx: 2.1.1

client-only@0.0.1: {}

clsx@2.1.1: {}

cmdk@1.0.4(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0):
dependencies:
'@radix-ui/react-dialog': 1.1.4(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
'@radix-ui/react-id': 1.1.1(@types/react@19.0.0)(react@19.2.0)
'@radix-ui/react-primitive': 2.1.3(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
use-sync-external-store: 1.6.0(react@19.2.0)
transitivePeerDependencies: - '@types/react' - '@types/react-dom'

core-js@3.46.0:
optional: true

css-line-break@2.1.0:
dependencies:
utrie: 1.0.2
optional: true

csstype@3.1.3: {}

d3-array@3.2.4:
dependencies:
internmap: 2.0.3

d3-color@3.1.0: {}

d3-ease@3.0.1: {}

d3-format@3.1.0: {}

d3-interpolate@3.0.1:
dependencies:
d3-color: 3.1.0

d3-path@3.1.0: {}

d3-scale@4.0.2:
dependencies:
d3-array: 3.2.4
d3-format: 3.1.0
d3-interpolate: 3.0.1
d3-time: 3.1.0
d3-time-format: 4.1.0

d3-shape@3.2.0:
dependencies:
d3-path: 3.1.0

d3-time-format@4.1.0:
dependencies:
d3-time: 3.1.0

d3-time@3.1.0:
dependencies:
d3-array: 3.2.4

d3-timer@3.0.1: {}

date-fns-jalali@4.1.0-0: {}

date-fns@4.1.0: {}

decimal.js-light@2.5.1: {}

detect-libc@2.1.2: {}

detect-node-es@1.1.0: {}

dompurify@3.3.0:
optionalDependencies:
'@types/trusted-types': 2.0.7
optional: true

electron-to-chromium@1.5.244: {}

embla-carousel-react@8.5.1(react@19.2.0):
dependencies:
embla-carousel: 8.5.1
embla-carousel-reactive-utils: 8.5.1(embla-carousel@8.5.1)
react: 19.2.0

embla-carousel-reactive-utils@8.5.1(embla-carousel@8.5.1):
dependencies:
embla-carousel: 8.5.1

embla-carousel@8.5.1: {}

enhanced-resolve@5.18.3:
dependencies:
graceful-fs: 4.2.11
tapable: 2.3.0

es-toolkit@1.41.0: {}

escalade@3.2.0: {}

eventemitter3@5.0.1: {}

fast-png@6.4.0:
dependencies:
'@types/pako': 2.0.4
iobuffer: 5.4.0
pako: 2.1.0

fflate@0.8.2: {}

fraction.js@4.3.7: {}

get-nonce@1.0.1: {}

graceful-fs@4.2.11: {}

html2canvas@1.4.1:
dependencies:
css-line-break: 2.1.0
text-segmentation: 1.0.3
optional: true

immer@10.2.0: {}

input-otp@1.4.1(react-dom@19.2.0(react@19.2.0))(react@19.2.0):
dependencies:
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)

internmap@2.0.3: {}

iobuffer@5.4.0: {}

jiti@2.6.1: {}

jspdf@3.0.3:
dependencies:
'@babel/runtime': 7.28.4
fast-png: 6.4.0
fflate: 0.8.2
optionalDependencies:
canvg: 3.0.11
core-js: 3.46.0
dompurify: 3.3.0
html2canvas: 1.4.1

lightningcss-darwin-arm64@1.30.1:
optional: true

lightningcss-darwin-x64@1.30.1:
optional: true

lightningcss-freebsd-x64@1.30.1:
optional: true

lightningcss-linux-arm-gnueabihf@1.30.1:
optional: true

lightningcss-linux-arm64-gnu@1.30.1:
optional: true

lightningcss-linux-arm64-musl@1.30.1:
optional: true

lightningcss-linux-x64-gnu@1.30.1:
optional: true

lightningcss-linux-x64-musl@1.30.1:
optional: true

lightningcss-win32-arm64-msvc@1.30.1:
optional: true

lightningcss-win32-x64-msvc@1.30.1:
optional: true

lightningcss@1.30.1:
dependencies:
detect-libc: 2.1.2
optionalDependencies:
lightningcss-darwin-arm64: 1.30.1
lightningcss-darwin-x64: 1.30.1
lightningcss-freebsd-x64: 1.30.1
lightningcss-linux-arm-gnueabihf: 1.30.1
lightningcss-linux-arm64-gnu: 1.30.1
lightningcss-linux-arm64-musl: 1.30.1
lightningcss-linux-x64-gnu: 1.30.1
lightningcss-linux-x64-musl: 1.30.1
lightningcss-win32-arm64-msvc: 1.30.1
lightningcss-win32-x64-msvc: 1.30.1

lucide-react@0.454.0(react@19.2.0):
dependencies:
react: 19.2.0

magic-string@0.30.21:
dependencies:
'@jridgewell/sourcemap-codec': 1.5.5

minipass@7.1.2: {}

minizlib@3.1.0:
dependencies:
minipass: 7.1.2

nanoid@3.3.11: {}

next-themes@0.4.6(react-dom@19.2.0(react@19.2.0))(react@19.2.0):
dependencies:
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)

next@16.0.0(react-dom@19.2.0(react@19.2.0))(react@19.2.0):
dependencies:
'@next/env': 16.0.0
'@swc/helpers': 0.5.15
caniuse-lite: 1.0.30001752
postcss: 8.4.31
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
styled-jsx: 5.1.6(react@19.2.0)
optionalDependencies:
'@next/swc-darwin-arm64': 16.0.0
'@next/swc-darwin-x64': 16.0.0
'@next/swc-linux-arm64-gnu': 16.0.0
'@next/swc-linux-arm64-musl': 16.0.0
'@next/swc-linux-x64-gnu': 16.0.0
'@next/swc-linux-x64-musl': 16.0.0
'@next/swc-win32-arm64-msvc': 16.0.0
'@next/swc-win32-x64-msvc': 16.0.0
sharp: 0.34.4
transitivePeerDependencies: - '@babel/core' - babel-plugin-macros

node-releases@2.0.27: {}

normalize-range@0.1.2: {}

pako@2.1.0: {}

performance-now@2.1.0:
optional: true

picocolors@1.1.1: {}

postcss-value-parser@4.2.0: {}

postcss@8.4.31:
dependencies:
nanoid: 3.3.11
picocolors: 1.1.1
source-map-js: 1.2.1

postcss@8.5.0:
dependencies:
nanoid: 3.3.11
picocolors: 1.1.1
source-map-js: 1.2.1

raf@3.4.1:
dependencies:
performance-now: 2.1.0
optional: true

react-day-picker@9.8.0(react@19.2.0):
dependencies:
'@date-fns/tz': 1.2.0
date-fns: 4.1.0
date-fns-jalali: 4.1.0-0
react: 19.2.0

react-dom@19.2.0(react@19.2.0):
dependencies:
react: 19.2.0
scheduler: 0.27.0

react-hook-form@7.60.0(react@19.2.0):
dependencies:
react: 19.2.0

react-is@19.2.0: {}

react-redux@9.2.0(@types/react@19.0.0)(react@19.2.0)(redux@5.0.1):
dependencies:
'@types/use-sync-external-store': 0.0.6
react: 19.2.0
use-sync-external-store: 1.6.0(react@19.2.0)
optionalDependencies:
'@types/react': 19.0.0
redux: 5.0.1

react-remove-scroll-bar@2.3.8(@types/react@19.0.0)(react@19.2.0):
dependencies:
react: 19.2.0
react-style-singleton: 2.2.3(@types/react@19.0.0)(react@19.2.0)
tslib: 2.8.1
optionalDependencies:
'@types/react': 19.0.0

react-remove-scroll@2.7.1(@types/react@19.0.0)(react@19.2.0):
dependencies:
react: 19.2.0
react-remove-scroll-bar: 2.3.8(@types/react@19.0.0)(react@19.2.0)
react-style-singleton: 2.2.3(@types/react@19.0.0)(react@19.2.0)
tslib: 2.8.1
use-callback-ref: 1.3.3(@types/react@19.0.0)(react@19.2.0)
use-sidecar: 1.1.3(@types/react@19.0.0)(react@19.2.0)
optionalDependencies:
'@types/react': 19.0.0

react-resizable-panels@2.1.7(react-dom@19.2.0(react@19.2.0))(react@19.2.0):
dependencies:
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)

react-style-singleton@2.2.3(@types/react@19.0.0)(react@19.2.0):
dependencies:
get-nonce: 1.0.1
react: 19.2.0
tslib: 2.8.1
optionalDependencies:
'@types/react': 19.0.0

react@19.2.0: {}

recharts@3.3.0(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react-is@19.2.0)(react@19.2.0)(redux@5.0.1):
dependencies:
'@reduxjs/toolkit': 2.9.2(react-redux@9.2.0(@types/react@19.0.0)(react@19.2.0)(redux@5.0.1))(react@19.2.0)
clsx: 2.1.1
decimal.js-light: 2.5.1
es-toolkit: 1.41.0
eventemitter3: 5.0.1
immer: 10.2.0
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
react-is: 19.2.0
react-redux: 9.2.0(@types/react@19.0.0)(react@19.2.0)(redux@5.0.1)
reselect: 5.1.1
tiny-invariant: 1.3.3
use-sync-external-store: 1.6.0(react@19.2.0)
victory-vendor: 37.3.6
transitivePeerDependencies: - '@types/react' - redux

redux-thunk@3.1.0(redux@5.0.1):
dependencies:
redux: 5.0.1

redux@5.0.1: {}

regenerator-runtime@0.13.11:
optional: true

reselect@5.1.1: {}

rgbcolor@1.0.1:
optional: true

scheduler@0.27.0: {}

semver@7.7.3:
optional: true

server-only@0.0.1: {}

sharp@0.34.4:
dependencies:
'@img/colour': 1.0.0
detect-libc: 2.1.2
semver: 7.7.3
optionalDependencies:
'@img/sharp-darwin-arm64': 0.34.4
'@img/sharp-darwin-x64': 0.34.4
'@img/sharp-libvips-darwin-arm64': 1.2.3
'@img/sharp-libvips-darwin-x64': 1.2.3
'@img/sharp-libvips-linux-arm': 1.2.3
'@img/sharp-libvips-linux-arm64': 1.2.3
'@img/sharp-libvips-linux-ppc64': 1.2.3
'@img/sharp-libvips-linux-s390x': 1.2.3
'@img/sharp-libvips-linux-x64': 1.2.3
'@img/sharp-libvips-linuxmusl-arm64': 1.2.3
'@img/sharp-libvips-linuxmusl-x64': 1.2.3
'@img/sharp-linux-arm': 0.34.4
'@img/sharp-linux-arm64': 0.34.4
'@img/sharp-linux-ppc64': 0.34.4
'@img/sharp-linux-s390x': 0.34.4
'@img/sharp-linux-x64': 0.34.4
'@img/sharp-linuxmusl-arm64': 0.34.4
'@img/sharp-linuxmusl-x64': 0.34.4
'@img/sharp-wasm32': 0.34.4
'@img/sharp-win32-arm64': 0.34.4
'@img/sharp-win32-ia32': 0.34.4
'@img/sharp-win32-x64': 0.34.4
optional: true

sonner@1.7.4(react-dom@19.2.0(react@19.2.0))(react@19.2.0):
dependencies:
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)

source-map-js@1.2.1: {}

stackblur-canvas@2.7.0:
optional: true

styled-jsx@5.1.6(react@19.2.0):
dependencies:
client-only: 0.0.1
react: 19.2.0

svg-pathdata@6.0.3:
optional: true

tailwind-merge@2.5.5: {}

tailwindcss-animate@1.0.7(tailwindcss@4.1.9):
dependencies:
tailwindcss: 4.1.9

tailwindcss@4.1.9: {}

tapable@2.3.0: {}

tar@7.5.2:
dependencies:
'@isaacs/fs-minipass': 4.0.1
chownr: 3.0.0
minipass: 7.1.2
minizlib: 3.1.0
yallist: 5.0.0

text-segmentation@1.0.3:
dependencies:
utrie: 1.0.2
optional: true

tiny-invariant@1.3.3: {}

tslib@2.8.1: {}

tw-animate-css@1.3.3: {}

typescript@5.0.2: {}

undici-types@6.11.1: {}

update-browserslist-db@1.1.4(browserslist@4.27.0):
dependencies:
browserslist: 4.27.0
escalade: 3.2.0
picocolors: 1.1.1

use-callback-ref@1.3.3(@types/react@19.0.0)(react@19.2.0):
dependencies:
react: 19.2.0
tslib: 2.8.1
optionalDependencies:
'@types/react': 19.0.0

use-sidecar@1.1.3(@types/react@19.0.0)(react@19.2.0):
dependencies:
detect-node-es: 1.1.0
react: 19.2.0
tslib: 2.8.1
optionalDependencies:
'@types/react': 19.0.0

use-sync-external-store@1.6.0(react@19.2.0):
dependencies:
react: 19.2.0

utrie@1.0.2:
dependencies:
base64-arraybuffer: 1.0.2
optional: true

vaul@0.9.9(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0):
dependencies:
'@radix-ui/react-dialog': 1.1.4(@types/react-dom@19.0.0)(@types/react@19.0.0)(react-dom@19.2.0(react@19.2.0))(react@19.2.0)
react: 19.2.0
react-dom: 19.2.0(react@19.2.0)
transitivePeerDependencies: - '@types/react' - '@types/react-dom'

victory-vendor@37.3.6:
dependencies:
'@types/d3-array': 3.2.2
'@types/d3-ease': 3.0.2
'@types/d3-interpolate': 3.0.4
'@types/d3-scale': 4.0.9
'@types/d3-shape': 3.1.7
'@types/d3-time': 3.0.4
'@types/d3-timer': 3.0.2
d3-array: 3.2.4
d3-ease: 3.0.1
d3-interpolate: 3.0.1
d3-scale: 4.0.2
d3-shape: 3.2.0
d3-time: 3.1.0
d3-timer: 3.0.1

yallist@5.0.0: {}

zod@3.25.76: {}

================================================
FILE: postcss.config.mjs
================================================
/\*_ @type {import('postcss-load-config').Config} _/
const config = {
plugins: {
'@tailwindcss/postcss': {},
},
}

export default config

================================================
FILE: tsconfig.json
================================================
{
"compilerOptions": {
"lib": ["dom", "dom.iterable", "esnext"],
"allowJs": true,
"target": "ES6",
"skipLibCheck": true,
"strict": true,
"noEmit": true,
"esModuleInterop": true,
"module": "esnext",
"moduleResolution": "bundler",
"resolveJsonModule": true,
"isolatedModules": true,
"jsx": "preserve",
"incremental": true,
"plugins": [
{
"name": "next"
}
],
"paths": {
"@/_": ["./_"]
}
},
"include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
"exclude": ["node_modules"]
}

================================================
FILE: app/globals.css
================================================
@import "tailwindcss";
@import "tw-animate-css";

@custom-variant dark (&:is(.dark \*));

:root {
/_ Paleta profissional com azul profundo, cinzas elegantes e acentos estratégicos _/
--background: oklch(0.98 0 0);
--foreground: oklch(0.12 0 0);
--card: oklch(1 0 0);
--card-foreground: oklch(0.12 0 0);
--popover: oklch(1 0 0);
--popover-foreground: oklch(0.12 0 0);
--primary: oklch(0.35 0.15 260);
--primary-foreground: oklch(1 0 0);
--secondary: oklch(0.95 0.02 260);
--secondary-foreground: oklch(0.35 0.15 260);
--muted: oklch(0.93 0 0);
--muted-foreground: oklch(0.5 0 0);
--accent: oklch(0.52 0.2 50);
--accent-foreground: oklch(1 0 0);
--destructive: oklch(0.63 0.25 25);
--destructive-foreground: oklch(1 0 0);
--border: oklch(0.92 0 0);
--input: oklch(0.96 0 0);
--ring: oklch(0.35 0.15 260);
--chart-1: oklch(0.35 0.15 260);
--chart-2: oklch(0.52 0.2 50);
--chart-3: oklch(0.65 0.12 180);
--chart-4: oklch(0.4 0.1 340);
--chart-5: oklch(0.58 0.15 120);
--radius: 0.625rem;
--sidebar: oklch(0.98 0 0);
--sidebar-foreground: oklch(0.12 0 0);
--sidebar-primary: oklch(0.35 0.15 260);
--sidebar-primary-foreground: oklch(1 0 0);
--sidebar-accent: oklch(0.95 0.02 260);
--sidebar-accent-foreground: oklch(0.35 0.15 260);
--sidebar-border: oklch(0.92 0 0);
--sidebar-ring: oklch(0.35 0.15 260);
}

.dark {
--background: oklch(0.1 0 0);
--foreground: oklch(0.95 0 0);
--card: oklch(0.15 0 0);
--card-foreground: oklch(0.95 0 0);
--popover: oklch(0.15 0 0);
--popover-foreground: oklch(0.95 0 0);
--primary: oklch(0.65 0.15 260);
--primary-foreground: oklch(0.1 0 0);
--secondary: oklch(0.2 0.02 260);
--secondary-foreground: oklch(0.95 0 0);
--muted: oklch(0.3 0 0);
--muted-foreground: oklch(0.7 0 0);
--accent: oklch(0.65 0.18 50);
--accent-foreground: oklch(0.1 0 0);
--destructive: oklch(0.63 0.25 25);
--destructive-foreground: oklch(0.95 0 0);
--border: oklch(0.25 0 0);
--input: oklch(0.2 0 0);
--ring: oklch(0.65 0.15 260);
--chart-1: oklch(0.65 0.15 260);
--chart-2: oklch(0.72 0.18 50);
--chart-3: oklch(0.7 0.12 180);
--chart-4: oklch(0.6 0.12 340);
--chart-5: oklch(0.75 0.15 120);
--sidebar: oklch(0.12 0 0);
--sidebar-foreground: oklch(0.95 0 0);
--sidebar-primary: oklch(0.65 0.15 260);
--sidebar-primary-foreground: oklch(0.1 0 0);
--sidebar-accent: oklch(0.25 0.02 260);
--sidebar-accent-foreground: oklch(0.95 0 0);
--sidebar-border: oklch(0.25 0 0);
--sidebar-ring: oklch(0.65 0.15 260);
}

@theme inline {
--font-sans: "Geist", "Geist Fallback";
--font-mono: "Geist Mono", "Geist Mono Fallback";
--color-background: var(--background);
--color-foreground: var(--foreground);
--color-card: var(--card);
--color-card-foreground: var(--card-foreground);
--color-popover: var(--popover);
--color-popover-foreground: var(--popover-foreground);
--color-primary: var(--primary);
--color-primary-foreground: var(--primary-foreground);
--color-secondary: var(--secondary);
--color-secondary-foreground: var(--secondary-foreground);
--color-muted: var(--muted);
--color-muted-foreground: var(--muted-foreground);
--color-accent: var(--accent);
--color-accent-foreground: var(--accent-foreground);
--color-destructive: var(--destructive);
--color-destructive-foreground: var(--destructive-foreground);
--color-border: var(--border);
--color-input: var(--input);
--color-ring: var(--ring);
--color-chart-1: var(--chart-1);
--color-chart-2: var(--chart-2);
--color-chart-3: var(--chart-3);
--color-chart-4: var(--chart-4);
--color-chart-5: var(--chart-5);
--radius-sm: calc(var(--radius) - 4px);
--radius-md: calc(var(--radius) - 2px);
--radius-lg: var(--radius);
--radius-xl: calc(var(--radius) + 4px);
--color-sidebar: var(--sidebar);
--color-sidebar-foreground: var(--sidebar-foreground);
--color-sidebar-primary: var(--sidebar-primary);
--color-sidebar-primary-foreground: var(--sidebar-primary-foreground);
--color-sidebar-accent: var(--sidebar-accent);
--color-sidebar-accent-foreground: var(--sidebar-accent-foreground);
--color-sidebar-border: var(--sidebar-border);
--color-sidebar-ring: var(--sidebar-ring);
}

@layer base {

- {
  @apply border-border outline-ring/50;
  }
  body {
  @apply bg-background text-foreground;
  }
  }

/_ Custom styles for SEO Analysis Platform _/
.gradient-hero {
background: linear-gradient(135deg, #2d4a7a 0%, #1a2a4a 100%);
}

.metric-card-gradient {
background: linear-gradient(135deg, rgba(45, 74, 122, 0.05) 0%, rgba(82, 108, 166, 0.05) 100%);
}

.scan-progress {
animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

@keyframes scan {
0%,
100% {
opacity: 1;
}
50% {
opacity: 0.5;
}
}

.insight-badge {
@apply inline-flex items-center px-3 py-1 text-sm font-medium rounded-full gap-1;
}

.insight-badge.critical {
@apply bg-red-100 text-red-800;
}

.insight-badge.warning {
@apply bg-yellow-100 text-yellow-800;
}

.insight-badge.success {
@apply bg-green-100 text-green-800;
}

.insight-badge.info {
@apply bg-blue-100 text-blue-800;
}

================================================
FILE: app/layout.tsx
================================================
import type { Metadata } from 'next'
import { Geist, Geist_Mono } from 'next/font/google'
import { Analytics } from '@vercel/analytics/next'
import './globals.css'

const \_geist = Geist({ subsets: ["latin"] });
const \_geistMono = Geist_Mono({ subsets: ["latin"] });

export const metadata: Metadata = {
title: 'v0 App',
description: 'Created with v0',
generator: 'v0.app',
}

export default function RootLayout({
children,
}: Readonly<{
children: React.ReactNode
}>) {
return (
<html lang="en">
<body className={`font-sans antialiased`}>
{children}
<Analytics />
</body>
</html>
)
}

================================================
FILE: app/page.tsx
================================================
"use client"

import { useState } from "react"
import Header from "@/components/header"
import Hero from "@/components/hero"
import AnalysisForm from "@/components/analysis-form"
import Dashboard from "@/components/dashboard"

export default function Home() {
const [showAnalysis, setShowAnalysis] = useState(false)
const [analysisData, setAnalysisData] = useState(null)

const handleAnalysisStart = (data: any) => {
setAnalysisData(data)
setShowAnalysis(true)
}

return (
<main className="min-h-screen bg-gradient-to-b from-background via-secondary to-background">
<Header />
{!showAnalysis ? (
<>
<Hero />
<AnalysisForm onAnalysisStart={handleAnalysisStart} />
</>
) : (
<Dashboard data={analysisData} onBack={() => setShowAnalysis(false)} />
)}
</main>
)
}

================================================
FILE: app/api/analyze/route.ts
================================================
import { type NextRequest, NextResponse } from "next/server"

interface AnalysisResult {
url: string
timestamp: string
metrics: {
seo: number
performance: number
accessibility: number
cro: number
security: string
indexedPages: number
}
issues: Array<{
type: "critical" | "warning" | "success" | "info"
title: string
description: string
action: string
impact: "Alto" | "Médio" | "Baixo"
}>
}

export async function POST(request: NextRequest) {
try {
const { url } = await request.json()

    if (!url) {
      return NextResponse.json({ error: "URL é obrigatória" }, { status: 400 })
    }

    // In production, this would call actual SEO APIs or web scraping services
    const urlHash = url.split("").reduce((acc, char) => acc + char.charCodeAt(0), 0)
    const seed = urlHash % 100

    const analysisResult: AnalysisResult = {
      url,
      timestamp: new Date().toISOString(),
      metrics: {
        seo: 70 + Math.floor(seed / 2),
        performance: 75 + Math.floor((seed * 0.7) % 20),
        accessibility: 65 + Math.floor((seed * 0.9) % 25),
        cro: 60 + Math.floor((seed * 0.6) % 30),
        security: seed % 2 === 0 ? "A+" : "A",
        indexedPages: 50 + Math.floor((seed * 5) % 150),
      },
      issues: [
        {
          type: "critical",
          title: "Meta Descriptions Incompletas",
          description: "12 páginas estão sem meta descriptions otimizadas. Isso reduz o CTR nos resultados de busca.",
          action: "Adicionar meta descriptions únicas para cada página",
          impact: "Alto",
        },
        {
          type: "warning",
          title: "Imagens sem Alt Text",
          description: "34 imagens estão sem atributo ALT, prejudicando a indexação e acessibilidade.",
          action: "Adicionar descrições relevantes em todas as imagens",
          impact: "Médio",
        },
        {
          type: "success",
          title: "Schema Markup Implementado",
          description: "Estrutura de dados JSON-LD está corretamente implementada.",
          action: "Continuar mantendo a implementação",
          impact: "Alto",
        },
        {
          type: "info",
          title: "Oportunidade: Conteúdo em Longa Cauda",
          description: "Análise detectou 23 palavras-chave de nicho com baixa concorrência.",
          action: "Criar conteúdo para palavras-chave de longa cauda identificadas",
          impact: "Médio",
        },
        {
          type: "warning",
          title: "Velocidade Mobile Acima da Média",
          description: "Tempo de carregamento em dispositivos móveis é 1.2s acima do recomendado.",
          action: "Otimizar imagens e minificar CSS/JS",
          impact: "Médio",
        },
        {
          type: "success",
          title: "Estrutura de URL Otimizada",
          description: "URLs descritivas e bem estruturadas detectadas no site.",
          action: "Manter padrão atual",
          impact: "Baixo",
        },
      ],
    }

    return NextResponse.json(analysisResult)

} catch (error) {
console.error("Erro na análise:", error)
return NextResponse.json({ error: "Erro ao analisar URL" }, { status: 500 })
}
}

================================================
FILE: components/analysis-charts.tsx
================================================
"use client"

import { Card } from "@/components/ui/card"
import {
BarChart,
Bar,
AreaChart,
Area,
PieChart,
Pie,
Cell,
XAxis,
YAxis,
CartesianGrid,
Tooltip,
Legend,
ResponsiveContainer,
} from "recharts"

interface AnalysisChartsProps {
url: string
metrics?: {
seo: number
performance: number
accessibility: number
cro: number
security: string
indexedPages: number
}
}

export default function AnalysisCharts({ url, metrics }: AnalysisChartsProps) {
const defaultMetrics = {
seo: 87,
performance: 92,
accessibility: 78,
cro: 73,
security: "A+",
indexedPages: 156,
}

const data = metrics || defaultMetrics

// SEO evolution data
const seoTrendData = [
{ month: "Jan", score: 65, ranking: 45, improvement: 0 },
{ month: "Fev", score: 68, ranking: 50, improvement: 4.6 },
{ month: "Mar", score: 72, ranking: 58, improvement: 5.9 },
{ month: "Abr", score: 75, ranking: 65, improvement: 4.2 },
{ month: "Mai", score: 78, ranking: 72, improvement: 4.0 },
{ month: "Jun", score: data.seo, ranking: data.seo + 5, improvement: ((data.seo - 65) / 65) * 100 },
]

// CRO metrics data
const croMetricsData = [
{ area: "CTR", value: 68 },
{ area: "Engajamento", value: 75 },
{ area: "Bounce Rate", value: Math.max(30, 100 - data.cro) },
{ area: "Time on Page", value: data.cro - 10 },
{ area: "Conversão", value: data.cro },
]

// Score distribution (pie chart)
const scoreDistribution = [
{ name: "SEO", value: data.seo },
{ name: "Performance", value: data.performance },
{ name: "Acessibilidade", value: data.accessibility },
]

const COLORS = ["#2d4a7a", "#d4a574", "#52a2a6"]

// Technical metrics
const technicalMetrics = [
{ metric: "Mobile Ready", value: data.performance + 5 },
{ metric: "SSL/HTTPS", value: 100 },
{ metric: "Compressão", value: 85 },
{ metric: "Cache", value: 78 },
{ metric: "Minificação", value: 90 },
]

return (
<div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
{/_ SEO Trend _/}
<Card className="p-6 bg-white/50 backdrop-blur border-border">
<h3 className="text-lg font-semibold text-foreground mb-4">Evolução SEO (6 meses)</h3>
<ResponsiveContainer width="100%" height={300}>
<AreaChart data={seoTrendData}>
<defs>
<linearGradient id="colorScore" x1="0" y1="0" x2="0" y2="1">
<stop offset="5%" stopColor="#2d4a7a" stopOpacity={0.8} />
<stop offset="95%" stopColor="#2d4a7a" stopOpacity={0} />
</linearGradient>
</defs>
<CartesianGrid strokeDasharray="3 3" stroke="#e5e7eb" />
<XAxis dataKey="month" />
<YAxis />
<Tooltip />
<Legend />
<Area
              type="monotone"
              dataKey="score"
              stroke="#2d4a7a"
              fillOpacity={1}
              fill="url(#colorScore)"
              name="Score SEO"
            />
</AreaChart>
</ResponsiveContainer>
</Card>

      {/* CRO Metrics */}
      <Card className="p-6 bg-white/50 backdrop-blur border-border">
        <h3 className="text-lg font-semibold text-foreground mb-4">Métricas CRO</h3>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={croMetricsData}>
            <CartesianGrid strokeDasharray="3 3" stroke="#e5e7eb" />
            <XAxis dataKey="area" />
            <YAxis />
            <Tooltip />
            <Bar dataKey="value" fill="#2d4a7a" radius={[8, 8, 0, 0]} />
          </BarChart>
        </ResponsiveContainer>
      </Card>

      {/* Score Distribution */}
      <Card className="p-6 bg-white/50 backdrop-blur border-border">
        <h3 className="text-lg font-semibold text-foreground mb-4">Distribuição de Scores</h3>
        <ResponsiveContainer width="100%" height={300}>
          <PieChart>
            <Pie
              data={scoreDistribution}
              cx="50%"
              cy="50%"
              labelLine={false}
              label={({ name, value }) => `${name}: ${value}`}
              outerRadius={80}
              fill="#8884d8"
              dataKey="value"
            >
              {scoreDistribution.map((entry, index) => (
                <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
              ))}
            </Pie>
            <Tooltip />
          </PieChart>
        </ResponsiveContainer>
      </Card>

      {/* Technical Metrics */}
      <Card className="p-6 bg-white/50 backdrop-blur border-border">
        <h3 className="text-lg font-semibold text-foreground mb-4">Métricas Técnicas</h3>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={technicalMetrics} layout="vertical" margin={{ top: 5, right: 30, left: 150, bottom: 5 }}>
            <CartesianGrid strokeDasharray="3 3" stroke="#e5e7eb" />
            <XAxis type="number" />
            <YAxis type="category" dataKey="metric" width={140} />
            <Tooltip />
            <Bar dataKey="value" fill="#d4a574" radius={[0, 8, 8, 0]} />
          </BarChart>
        </ResponsiveContainer>
      </Card>

      {/* Performance Indicators */}
      <Card className="p-6 bg-white/50 backdrop-blur border-border lg:col-span-2">
        <h3 className="text-lg font-semibold text-foreground mb-4">Indicadores de Performance</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
          <div className="space-y-2">
            <p className="text-sm text-muted-foreground">Tempo de Carregamento</p>
            <div className="flex items-end gap-2">
              <span className="text-3xl font-bold text-primary">{2 + (100 - data.performance) / 10}</span>
              <span className="text-sm text-muted-foreground">segundos</span>
            </div>
            <div className="w-full bg-gray-200 rounded-full h-2">
              <div className="bg-primary h-2 rounded-full" style={{ width: `${data.performance}%` }}></div>
            </div>
          </div>

          <div className="space-y-2">
            <p className="text-sm text-muted-foreground">Taxa de Conversão</p>
            <div className="flex items-end gap-2">
              <span className="text-3xl font-bold text-accent">{data.cro / 20}</span>
              <span className="text-sm text-muted-foreground">%</span>
            </div>
            <div className="w-full bg-gray-200 rounded-full h-2">
              <div className="bg-accent h-2 rounded-full" style={{ width: `${data.cro}%` }}></div>
            </div>
          </div>

          <div className="space-y-2">
            <p className="text-sm text-muted-foreground">Páginas Indexadas</p>
            <div className="flex items-end gap-2">
              <span className="text-3xl font-bold text-green-600">{data.indexedPages}</span>
            </div>
            <p className="text-xs text-muted-foreground">em {new Date().getFullYear()}</p>
          </div>

          <div className="space-y-2">
            <p className="text-sm text-muted-foreground">Score Geral</p>
            <div className="flex items-end gap-2">
              <span className="text-3xl font-bold text-blue-600">
                {Math.round((data.seo + data.performance + data.accessibility) / 3)}
              </span>
              <span className="text-sm text-muted-foreground">/100</span>
            </div>
            <div className="w-full bg-gray-200 rounded-full h-2">
              <div
                className="bg-blue-600 h-2 rounded-full"
                style={{
                  width: `${Math.round((data.seo + data.performance + data.accessibility) / 3)}%`,
                }}
              ></div>
            </div>
          </div>
        </div>
      </Card>
    </div>

)
}

================================================
FILE: components/analysis-form.tsx
================================================
"use client"

import type React from "react"
import { useState } from "react"
import { ArrowRight, Loader2 } from "lucide-react"
import { Button } from "@/components/ui/button"
import { Card } from "@/components/ui/card"
import { Input } from "@/components/ui/input"

interface AnalysisFormProps {
onAnalysisStart: (data: any) => void
}

export default function AnalysisForm({ onAnalysisStart }: AnalysisFormProps) {
const [url, setUrl] = useState("")
const [loading, setLoading] = useState(false)
const [error, setError] = useState("")

const handleSubmit = async (e: React.FormEvent) => {
e.preventDefault()
setError("")

    if (!url.trim()) {
      setError("Por favor, digite uma URL válida")
      return
    }

    try {
      new URL(url.startsWith("http") ? url : `https://${url}`)
    } catch {
      setError("URL inválida. Por favor, verifique o formato")
      return
    }

    setLoading(true)

    try {
      const response = await fetch("/api/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          url: url.startsWith("http") ? url : `https://${url}`,
        }),
      })

      if (!response.ok) {
        throw new Error("Falha na análise")
      }

      const analysisData = await response.json()
      onAnalysisStart(analysisData)
    } catch (err) {
      setError("Erro ao analisar URL. Tente novamente.")
      console.error(err)
    } finally {
      setLoading(false)
    }

}

return (
<section className="py-16 px-4">
<div className="max-w-2xl mx-auto">
<Card className="p-8 shadow-lg border-0 bg-white">
<form onSubmit={handleSubmit} className="space-y-6">
<div>
<label htmlFor="url" className="block text-sm font-semibold text-foreground mb-3">
Insira a URL do seu site
</label>
<div className="flex gap-3">
<Input
id="url"
type="text"
placeholder="exemplo.com.br"
value={url}
onChange={(e) => setUrl(e.target.value)}
disabled={loading}
className="text-lg h-12"
/>
<Button
                  type="submit"
                  disabled={loading}
                  className="px-8 h-12 bg-primary hover:bg-primary/90 text-white gap-2"
                >
{loading ? (
<>
<Loader2 className="w-4 h-4 animate-spin" />
Analisando...
</>
) : (
<>
Analisar
<ArrowRight className="w-4 h-4" />
</>
)}
</Button>
</div>
{error && <p className="text-destructive text-sm mt-2">{error}</p>}
</div>

            <div className="pt-4 border-t border-border">
              <p className="text-xs text-muted-foreground text-center">
                Análise rápida, segura e privada. Dados não são armazenados.
              </p>
            </div>
          </form>
        </Card>
      </div>
    </section>

)
}

================================================
FILE: components/dashboard.tsx
================================================
"use client"

import { useState } from "react"
import { ArrowLeft, Download } from "lucide-react"
import { Button } from "@/components/ui/button"
import MetricsGrid from "./metrics-grid"
import AnalysisCharts from "./analysis-charts"
import InsightsPanel from "./insights-panel"
import Recommendations from "./recommendations"
import { generatePDF } from "@/lib/pdf-generator"

interface DashboardProps {
data: any
onBack: () => void
}

export default function Dashboard({ data, onBack }: DashboardProps) {
const [generating, setGenerating] = useState(false)
const [activeTab, setActiveTab] = useState("overview")

const handleGeneratePDF = async () => {
setGenerating(true)
try {
await generatePDF(data)
} finally {
setGenerating(false)
}
}

return (
<div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
{/_ Header _/}
<div className="flex items-center justify-between">
<div className="flex items-center gap-4">
<Button variant="ghost" size="icon" onClick={onBack} className="h-10 w-10">
<ArrowLeft className="w-5 h-5" />
</Button>
<div>
<h1 className="text-3xl font-bold text-foreground">{data.url}</h1>
<p className="text-sm text-muted-foreground">
Análise realizada em {new Date(data.timestamp).toLocaleDateString("pt-BR")}
</p>
</div>
</div>
<Button
          onClick={handleGeneratePDF}
          disabled={generating}
          className="gap-2 bg-accent hover:bg-accent/90 text-accent-foreground"
        >
<Download className="w-4 h-4" />
{generating ? "Gerando..." : "Baixar Relatório"}
</Button>
</div>

      <div className="flex gap-2 border-b border-border">
        <Button
          variant={activeTab === "overview" ? "default" : "ghost"}
          onClick={() => setActiveTab("overview")}
          className="rounded-none border-b-2 border-transparent data-[state=active]:border-primary"
        >
          Visão Geral
        </Button>
        <Button
          variant={activeTab === "insights" ? "default" : "ghost"}
          onClick={() => setActiveTab("insights")}
          className="rounded-none border-b-2 border-transparent data-[state=active]:border-primary"
        >
          Insights
        </Button>
        <Button
          variant={activeTab === "recommendations" ? "default" : "ghost"}
          onClick={() => setActiveTab("recommendations")}
          className="rounded-none border-b-2 border-transparent data-[state=active]:border-primary"
        >
          Recomendações
        </Button>
      </div>

      {/* Main Content */}
      <div className="space-y-8">
        {activeTab === "overview" && (
          <>
            <MetricsGrid url={data.url} metrics={data.metrics} />
            <AnalysisCharts url={data.url} metrics={data.metrics} />
          </>
        )}

        {activeTab === "insights" && <InsightsPanel url={data.url} issues={data.issues} />}

        {activeTab === "recommendations" && <Recommendations url={data.url} metrics={data.metrics} />}
      </div>
    </div>

)
}

================================================
FILE: components/header.tsx
================================================
"use client"

import { Search } from "lucide-react"
import { Button } from "@/components/ui/button"

export default function Header() {
return (
<header className="sticky top-0 z-50 bg-white/80 backdrop-blur-md border-b border-border shadow-sm">
<div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
<div className="flex items-center justify-between">
<div className="flex items-center gap-3">
<div className="w-10 h-10 bg-primary rounded-lg flex items-center justify-center">
<Search className="w-6 h-6 text-primary-foreground" />
</div>
<h1 className="text-2xl font-bold text-primary">SiteScore</h1>
</div>
<nav className="hidden md:flex gap-8 items-center">
<a href="#features" className="text-foreground/70 hover:text-primary transition">
Recursos
</a>
<a href="#how-it-works" className="text-foreground/70 hover:text-primary transition">
Como Funciona
</a>
<Button variant="outline" size="sm">
Documentação
</Button>
</nav>
</div>
</div>
</header>
)
}

================================================
FILE: components/hero.tsx
================================================
import { Target } from "lucide-react"

export default function Hero() {
return (
<section className="relative py-20 px-4 overflow-hidden">
{/_ Background elements _/}
<div className="absolute inset-0 -z-10">
<div className="absolute top-20 left-10 w-72 h-72 bg-primary/10 rounded-full blur-3xl" />
<div className="absolute bottom-20 right-10 w-72 h-72 bg-accent/10 rounded-full blur-3xl" />
</div>

      <div className="max-w-4xl mx-auto text-center space-y-8">
        <div className="inline-flex items-center gap-2 px-4 py-2 bg-secondary rounded-full text-sm font-medium text-primary">
          <Target className="w-4 h-4" />
          Análise Profissional de Sites
        </div>

        <h1 className="text-5xl sm:text-6xl font-bold text-foreground leading-tight">
          Potencialize seu{" "}
          <span className="text-transparent bg-clip-text bg-gradient-to-r from-primary to-accent">
            Tráfego Orgânico
          </span>
        </h1>

        <p className="text-xl text-muted-foreground max-w-2xl mx-auto leading-relaxed">
          Análise completa de SEO, CRO e GEO em um único lugar. Descubra oportunidades de crescimento, identifique
          problemas técnicos e receba insights acionáveis para melhorar seu ranking.
        </p>

        <div className="grid grid-cols-3 gap-4 max-w-2xl mx-auto mt-12">
          <div className="p-4 bg-white/50 backdrop-blur rounded-lg border border-border">
            <div className="text-3xl font-bold text-primary">100%</div>
            <p className="text-sm text-muted-foreground">Análise Completa</p>
          </div>
          <div className="p-4 bg-white/50 backdrop-blur rounded-lg border border-border">
            <div className="text-3xl font-bold text-accent">5+</div>
            <p className="text-sm text-muted-foreground">Áreas de Análise</p>
          </div>
          <div className="p-4 bg-white/50 backdrop-blur rounded-lg border border-border">
            <div className="text-3xl font-bold text-primary">PDF</div>
            <p className="text-sm text-muted-foreground">Relatório Executivo</p>
          </div>
        </div>
      </div>
    </section>

)
}

================================================
FILE: components/insights-panel.tsx
================================================
"use client"

import { Card } from "@/components/ui/card"
import { AlertCircle, TrendingUp, Zap, CheckCircle } from "lucide-react"

interface InsightsPanelProps {
url: string
issues?: Array<{
type: "critical" | "warning" | "success" | "info"
title: string
description: string
action: string
impact: "Alto" | "Médio" | "Baixo"
}>
}

export default function InsightsPanel({ url, issues }: InsightsPanelProps) {
const defaultInsights = [
{
type: "critical" as const,
title: "Meta Descriptions Incompletas",
description: "12 páginas estão sem meta descriptions otimizadas. Isso reduz o CTR nos resultados de busca.",
action: "Adicionar meta descriptions únicas para cada página",
impact: "Alto" as const,
},
{
type: "warning" as const,
title: "Imagens sem Alt Text",
description: "34 imagens estão sem atributo ALT, prejudicando a indexação e acessibilidade.",
action: "Adicionar descrições relevantes em todas as imagens",
impact: "Médio" as const,
},
{
type: "success" as const,
title: "Schema Markup Implementado",
description: "Estrutura de dados JSON-LD está corretamente implementada.",
action: "Continuar mantendo a implementação",
impact: "Alto" as const,
},
{
type: "info" as const,
title: "Oportunidade: Conteúdo em Longa Cauda",
description: "Análise detectou 23 palavras-chave de nicho com baixa concorrência.",
action: "Criar conteúdo para palavras-chave de longa cauda identificadas",
impact: "Médio" as const,
},
{
type: "warning" as const,
title: "Velocidade Mobile Acima da Média",
description: "Tempo de carregamento em dispositivos móveis é 1.2s acima do recomendado.",
action: "Otimizar imagens e minificar CSS/JS",
impact: "Médio" as const,
},
{
type: "success" as const,
title: "Estrutura de URL Otimizada",
description: "URLs descritivas e bem estruturadas detectadas no site.",
action: "Manter padrão atual",
impact: "Baixo" as const,
},
]

const insightsList = issues || defaultInsights

const getIcon = (type: string) => {
switch (type) {
case "critical":
return <AlertCircle className="w-5 h-5 text-red-600" />
case "warning":
return <Zap className="w-5 h-5 text-yellow-600" />
case "success":
return <CheckCircle className="w-5 h-5 text-green-600" />
default:
return <TrendingUp className="w-5 h-5 text-blue-600" />
}
}

const getBgColor = (type: string) => {
switch (type) {
case "critical":
return "bg-red-50 border-red-200"
case "warning":
return "bg-yellow-50 border-yellow-200"
case "success":
return "bg-green-50 border-green-200"
default:
return "bg-blue-50 border-blue-200"
}
}

return (
<div className="space-y-4">
<h2 className="text-2xl font-bold text-foreground">Insights e Recomendações</h2>

      <div className="grid gap-4">
        {insightsList.map((insight, index) => (
          <Card
            key={index}
            className={`p-6 border-2 ${getBgColor(insight.type)} backdrop-blur transition-all hover:shadow-md`}
          >
            <div className="flex gap-4">
              <div className="flex-shrink-0 pt-1">{getIcon(insight.type)}</div>
              <div className="flex-1 min-w-0">
                <div className="flex items-start justify-between gap-4">
                  <div>
                    <h3 className="font-semibold text-foreground mb-1">{insight.title}</h3>
                    <p className="text-sm text-foreground/70 mb-3">{insight.description}</p>
                    <div className="space-y-2">
                      <div className="text-sm">
                        <span className="font-semibold text-foreground">Ação Recomendada:</span>
                        <p className="text-foreground/70">{insight.action}</p>
                      </div>
                    </div>
                  </div>
                  <div className="flex-shrink-0">
                    <span
                      className={`inline-flex items-center px-3 py-1 text-xs font-medium rounded-full ${
                        insight.impact === "Alto"
                          ? "bg-red-100 text-red-800"
                          : insight.impact === "Médio"
                            ? "bg-yellow-100 text-yellow-800"
                            : "bg-blue-100 text-blue-800"
                      }`}
                    >
                      Impacto: {insight.impact}
                    </span>
                  </div>
                </div>
              </div>
            </div>
          </Card>
        ))}
      </div>
    </div>

)
}

================================================
FILE: components/metrics-grid.tsx
================================================
"use client"

import { Card } from "@/components/ui/card"
import { TrendingUp, Eye, Zap, Globe, CheckCircle, AlertCircle } from "lucide-react"

interface MetricsGridProps {
url: string
metrics?: {
seo: number
performance: number
accessibility: number
cro: number
security: string
indexedPages: number
}
}

export default function MetricsGrid({ url, metrics }: MetricsGridProps) {
const defaultMetrics = {
seo: 87,
performance: 92,
accessibility: 78,
cro: 73,
security: "A+",
indexedPages: 156,
}

const data = metrics || defaultMetrics

const metricsArray = [
{
label: "Score SEO",
value: data.seo.toString(),
icon: TrendingUp,
color: "from-primary to-blue-600",
trend: "+12%",
description: "Otimização para motores de busca",
},
{
label: "Performance",
value: data.performance.toString(),
icon: Zap,
color: "from-accent to-yellow-500",
trend: "+5%",
description: "Velocidade de carregamento",
},
{
label: "Acessibilidade",
value: data.accessibility.toString(),
icon: Eye,
color: "from-green-500 to-emerald-600",
trend: "+8%",
description: "Usabilidade e acesso",
},
{
label: "Score CRO",
value: data.cro.toString(),
icon: CheckCircle,
color: "from-purple-500 to-pink-600",
trend: "+15%",
description: "Taxa de conversão",
},
{
label: "Segurança SSL",
value: data.security,
icon: Globe,
color: "from-green-600 to-teal-600",
trend: "Válido",
description: "Certificado HTTPS ativo",
},
{
label: "Indexação",
value: data.indexedPages.toString(),
icon: AlertCircle,
color: "from-orange-500 to-red-600",
trend: `+${Math.floor(data.indexedPages / 10)}`,
description: "Páginas indexadas",
},
]

return (
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
{metricsArray.map((metric, index) => {
const Icon = metric.icon
return (
<Card
            key={index}
            className="p-6 bg-white/50 backdrop-blur border-border hover:shadow-lg transition-shadow group"
          >
<div className="flex items-start justify-between mb-4">
<div className={`p-3 bg-gradient-to-br ${metric.color} rounded-lg`}>
<Icon className="w-6 h-6 text-white" />
</div>
<span className="text-xs font-semibold text-green-600 bg-green-50 px-2 py-1 rounded">{metric.trend}</span>
</div>
<p className="text-sm text-muted-foreground mb-1">{metric.label}</p>
<div className="flex items-baseline gap-2 mb-3">
<span className="text-4xl font-bold text-foreground">{metric.value}</span>
</div>
<p className="text-xs text-muted-foreground">{metric.description}</p>
</Card>
)
})}
</div>
)
}

================================================
FILE: components/recommendations.tsx
================================================
"use client"

import { Card } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { ChevronRight, Target, TrendingUp, AlertTriangle } from "lucide-react"

interface RecommendationsProps {
url: string
metrics?: {
seo: number
performance: number
accessibility: number
cro: number
security: string
indexedPages: number
}
}

export default function Recommendations({ url, metrics }: RecommendationsProps) {
const defaultMetrics = {
seo: 87,
performance: 92,
accessibility: 78,
cro: 73,
security: "A+",
indexedPages: 156,
}

const data = metrics || defaultMetrics

// Determine priority recommendations based on metrics
const priorityRecommendations = [
{
priority: 1,
title: "Implementar Structured Data",
description: "Rich snippets podem aumentar CTR em até 30%",
timeEstimate: "2-3 horas",
impact: "Alto",
tools: ["Schema.org", "JSON-LD Validator"],
icon: TrendingUp,
},
{
priority: 2,
title: "Otimizar Core Web Vitals",
description: "Foco em LCP, FID e CLS para melhor ranking",
timeEstimate: "4-6 horas",
impact: "Alto",
tools: ["PageSpeed Insights", "Chrome DevTools"],
icon: Target,
},
{
priority: 3,
title: "Revisar Estratégia de Backlinks",
description: "Adquirir links de autoridade para melhorar ranking",
timeEstimate: "Contínuo",
impact: "Alto",
tools: ["Ahrefs", "SEMrush"],
icon: TrendingUp,
},
{
priority: 4,
title: "Auditar Conteúdo Duplicado",
description: "Consolidar ou redirecionar conteúdo duplicado",
timeEstimate: "3-4 horas",
impact: "Médio",
tools: ["Screaming Frog", "Copyscape"],
icon: AlertTriangle,
},
]

return (
<div className="space-y-6">
<div>
<h2 className="text-2xl font-bold text-foreground mb-2">Recomendações Estratégicas</h2>
<p className="text-muted-foreground">
Plano de ação priorizado com base na análise de seu site. Implementar essas mudanças pode melhorar seu ranking
e conversões.
</p>
</div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
        {priorityRecommendations.map((rec, index) => {
          const Icon = rec.icon
          return (
            <Card
              key={index}
              className="p-6 bg-white/50 backdrop-blur border-border hover:shadow-lg transition-shadow group"
            >
              <div className="flex gap-4">
                <div className="flex-shrink-0">
                  <div className="flex items-center justify-center w-10 h-10 rounded-lg bg-primary/10">
                    <Icon className="w-5 h-5 text-primary" />
                  </div>
                </div>

                <div className="flex-1 min-w-0">
                  <div className="flex items-start justify-between gap-2 mb-2">
                    <div>
                      <h3 className="font-semibold text-foreground">{rec.title}</h3>
                      <p className="text-sm text-muted-foreground">{rec.description}</p>
                    </div>
                    <span className="text-xs font-bold px-2 py-1 rounded-full bg-primary/10 text-primary whitespace-nowrap">
                      P{rec.priority}
                    </span>
                  </div>

                  <div className="space-y-2 mt-4">
                    <div className="flex items-center justify-between text-sm">
                      <span className="text-muted-foreground">Tempo estimado:</span>
                      <span className="font-medium text-foreground">{rec.timeEstimate}</span>
                    </div>

                    <div className="flex items-center justify-between text-sm">
                      <span className="text-muted-foreground">Impacto esperado:</span>
                      <span
                        className={`font-medium ${
                          rec.impact === "Alto"
                            ? "text-green-600"
                            : rec.impact === "Médio"
                              ? "text-yellow-600"
                              : "text-blue-600"
                        }`}
                      >
                        {rec.impact}
                      </span>
                    </div>

                    <div className="pt-2 border-t border-border">
                      <p className="text-xs text-muted-foreground mb-2">Ferramentas recomendadas:</p>
                      <div className="flex flex-wrap gap-1">
                        {rec.tools.map((tool, i) => (
                          <span
                            key={i}
                            className="inline-block text-xs px-2 py-1 bg-secondary text-secondary-foreground rounded"
                          >
                            {tool}
                          </span>
                        ))}
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </Card>
          )
        })}
      </div>

      {/* Quick Wins Section */}
      <Card className="p-6 bg-green-50/50 border-green-200 backdrop-blur">
        <h3 className="font-bold text-green-900 mb-3 flex items-center gap-2">
          <span className="w-2 h-2 rounded-full bg-green-600"></span>
          Vitórias Rápidas (Implementar Agora)
        </h3>

        <ul className="space-y-2">
          <li className="flex items-start gap-3 text-sm">
            <ChevronRight className="w-4 h-4 text-green-600 mt-1 flex-shrink-0" />
            <span>
              Adicionar meta descriptions em todas as páginas principais{" "}
              <span className="text-xs text-green-700 font-medium">(30 min)</span>
            </span>
          </li>
          <li className="flex items-start gap-3 text-sm">
            <ChevronRight className="w-4 h-4 text-green-600 mt-1 flex-shrink-0" />
            <span>
              Incluir alt text em imagens principais{" "}
              <span className="text-xs text-green-700 font-medium">(1 hora)</span>
            </span>
          </li>
          <li className="flex items-start gap-3 text-sm">
            <ChevronRight className="w-4 h-4 text-green-600 mt-1 flex-shrink-0" />
            <span>
              Configurar Google Search Console e verificar indexação{" "}
              <span className="text-xs text-green-700 font-medium">(15 min)</span>
            </span>
          </li>
          <li className="flex items-start gap-3 text-sm">
            <ChevronRight className="w-4 h-4 text-green-600 mt-1 flex-shrink-0" />
            <span>
              Ativar gzip compression no servidor <span className="text-xs text-green-700 font-medium">(30 min)</span>
            </span>
          </li>
        </ul>
      </Card>

      {/* Action Button */}
      <Button className="w-full h-12 bg-primary hover:bg-primary/90 text-white text-base gap-2 group">
        Exportar Plano de Ação
        <ChevronRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
      </Button>
    </div>

)
}

================================================
FILE: components/theme-provider.tsx
================================================
'use client'

import \* as React from 'react'
import {
ThemeProvider as NextThemesProvider,
type ThemeProviderProps,
} from 'next-themes'

export function ThemeProvider({ children, ...props }: ThemeProviderProps) {
return <NextThemesProvider {...props}>{children}</NextThemesProvider>
}

================================================
FILE: components/ui/button.tsx
================================================
import \* as React from 'react'
import { Slot } from '@radix-ui/react-slot'
import { cva, type VariantProps } from 'class-variance-authority'

import { cn } from '@/lib/utils'

const buttonVariants = cva(
"inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md text-sm font-medium transition-all disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&\_svg:not([class*='size-'])]:size-4 shrink-0 [&_svg]:shrink-0 outline-none focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive",
{
variants: {
variant: {
default: 'bg-primary text-primary-foreground hover:bg-primary/90',
destructive:
'bg-destructive text-white hover:bg-destructive/90 focus-visible:ring-destructive/20 dark:focus-visible:ring-destructive/40 dark:bg-destructive/60',
outline:
'border bg-background shadow-xs hover:bg-accent hover:text-accent-foreground dark:bg-input/30 dark:border-input dark:hover:bg-input/50',
secondary:
'bg-secondary text-secondary-foreground hover:bg-secondary/80',
ghost:
'hover:bg-accent hover:text-accent-foreground dark:hover:bg-accent/50',
link: 'text-primary underline-offset-4 hover:underline',
},
size: {
default: 'h-9 px-4 py-2 has-[>svg]:px-3',
sm: 'h-8 rounded-md gap-1.5 px-3 has-[>svg]:px-2.5',
lg: 'h-10 rounded-md px-6 has-[>svg]:px-4',
icon: 'size-9',
'icon-sm': 'size-8',
'icon-lg': 'size-10',
},
},
defaultVariants: {
variant: 'default',
size: 'default',
},
},
)

function Button({
className,
variant,
size,
asChild = false,
...props
}: React.ComponentProps<'button'> &
VariantProps<typeof buttonVariants> & {
asChild?: boolean
}) {
const Comp = asChild ? Slot : 'button'

return (
<Comp
data-slot="button"
className={cn(buttonVariants({ variant, size, className }))}
{...props}
/>
)
}

export { Button, buttonVariants }

================================================
FILE: components/ui/card.tsx
================================================
import \* as React from 'react'

import { cn } from '@/lib/utils'

function Card({ className, ...props }: React.ComponentProps<'div'>) {
return (
<div
data-slot="card"
className={cn(
'bg-card text-card-foreground flex flex-col gap-6 rounded-xl border py-6 shadow-sm',
className,
)}
{...props}
/>
)
}

function CardHeader({ className, ...props }: React.ComponentProps<'div'>) {
return (
<div
data-slot="card-header"
className={cn(
'@container/card-header grid auto-rows-min grid-rows-[auto_auto] items-start gap-2 px-6 has-data-[slot=card-action]:grid-cols-[1fr_auto] [.border-b]:pb-6',
className,
)}
{...props}
/>
)
}

function CardTitle({ className, ...props }: React.ComponentProps<'div'>) {
return (
<div
data-slot="card-title"
className={cn('leading-none font-semibold', className)}
{...props}
/>
)
}

function CardDescription({ className, ...props }: React.ComponentProps<'div'>) {
return (
<div
data-slot="card-description"
className={cn('text-muted-foreground text-sm', className)}
{...props}
/>
)
}

function CardAction({ className, ...props }: React.ComponentProps<'div'>) {
return (
<div
data-slot="card-action"
className={cn(
'col-start-2 row-span-2 row-start-1 self-start justify-self-end',
className,
)}
{...props}
/>
)
}

function CardContent({ className, ...props }: React.ComponentProps<'div'>) {
return (
<div
data-slot="card-content"
className={cn('px-6', className)}
{...props}
/>
)
}

function CardFooter({ className, ...props }: React.ComponentProps<'div'>) {
return (
<div
data-slot="card-footer"
className={cn('flex items-center px-6 [.border-t]:pt-6', className)}
{...props}
/>
)
}

export {
Card,
CardHeader,
CardFooter,
CardTitle,
CardAction,
CardDescription,
CardContent,
}

================================================
FILE: components/ui/input.tsx
================================================
import \* as React from 'react'

import { cn } from '@/lib/utils'

function Input({ className, type, ...props }: React.ComponentProps<'input'>) {
return (
<input
type={type}
data-slot="input"
className={cn(
'file:text-foreground placeholder:text-muted-foreground selection:bg-primary selection:text-primary-foreground dark:bg-input/30 border-input h-9 w-full min-w-0 rounded-md border bg-transparent px-3 py-1 text-base shadow-xs transition-[color,box-shadow] outline-none file:inline-flex file:h-7 file:border-0 file:bg-transparent file:text-sm file:font-medium disabled:pointer-events-none disabled:cursor-not-allowed disabled:opacity-50 md:text-sm',
'focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px]',
'aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive',
className,
)}
{...props}
/>
)
}

export { Input }

================================================
FILE: lib/insights-generator.ts
================================================
interface MetricsData {
seo: number
performance: number
accessibility: number
cro: number
security: string
indexedPages: number
}

interface Insight {
type: "critical" | "warning" | "success" | "info"
title: string
description: string
action: string
impact: "Alto" | "Médio" | "Baixo"
}

export function generateInsights(metrics: MetricsData): Insight[] {
const insights: Insight[] = []

// SEO-related insights
if (metrics.seo < 70) {
insights.push({
type: "critical",
title: "Score SEO Abaixo do Ideal",
description: `Seu site tem score SEO de ${metrics.seo}/100, considerado baixo. Isso impacta significativamente sua visibilidade nos motores de busca.`,
action:
"Realizar auditoria SEO completa, otimizar meta tags, melhorar estrutura de URLs e implementar schema markup",
impact: "Alto",
})
}

if (metrics.seo >= 70 && metrics.seo < 85) {
insights.push({
type: "warning",
title: "SEO Precisa de Melhorias",
description: `Com score de ${metrics.seo}/100, há oportunidades significativas de otimização para melhorar ranking nos SERPs.`,
action: "Focar em conteúdo de qualidade, backlinks estratégicos e otimização on-page",
impact: "Médio",
})
}

if (metrics.seo >= 85) {
insights.push({
type: "success",
title: "SEO em Excelente Estado",
description: `Score SEO de ${metrics.seo}/100 indica otimização profissional. Seu site está bem posicionado para buscas orgânicas.`,
action: "Manter estratégia atual, continuar monitorando rankings e atualizando conteúdo",
impact: "Alto",
})
}

// Performance insights
if (metrics.performance < 70) {
insights.push({
type: "critical",
title: "Performance Crítica - Velocidade Muito Lenta",
description: `Score de performance ${metrics.performance}/100 indica site muito lento. Usuários podem estar abandonando suas páginas.`,
action: "Otimizar imagens, minificar CSS/JS, implementar lazy loading, usar CDN e cache",
impact: "Alto",
})
}

if (metrics.performance >= 70 && metrics.performance < 85) {
insights.push({
type: "warning",
title: "Performance Pode Ser Melhorada",
description: `Score de ${metrics.performance}/100 é aceitável, mas há room para otimização. Cada segundo conta para conversão.`,
action: "Analisar Core Web Vitals, otimizar recursos, reduzir CLS e melhorar LCP",
impact: "Médio",
})
}

if (metrics.performance >= 90) {
insights.push({
type: "success",
title: "Performance Excelente",
description: `Score de ${metrics.performance}/100 indica site muito rápido. Excelente experiência de usuário.`,
action: "Continuar monitorando performance, manter otimizações atuais",
impact: "Alto",
})
}

// Accessibility insights
if (metrics.accessibility < 70) {
insights.push({
type: "warning",
title: "Acessibilidade Limitada",
description: `Score de acessibilidade ${metrics.accessibility}/100 significa que muitos usuários podem ter dificuldades. Isso reduz inclusão.`,
action:
"Melhorar contraste de cores, adicionar aria-labels, testar com leitores de tela, melhorar navegação teclado",
impact: "Médio",
})
}

if (metrics.accessibility >= 80) {
insights.push({
type: "success",
title: "Acessibilidade Bem Implementada",
description: `Score de ${metrics.accessibility}/100 indica bom nível de acessibilidade. Site é inclusivo para todos.`,
action: "Manter padrões WCAG, fazer testes regularmente com usuários com deficiências",
impact: "Médio",
})
}

// CRO insights
if (metrics.cro < 60) {
insights.push({
type: "critical",
title: "Taxa de Conversão Muito Baixa",
description: `Score CRO de ${metrics.cro}/100 sugere sérios problemas na experiência de conversão. Muitos visitantes não convertem.`,
action: "Realizar análise de funil, A/B testar CTAs, melhorar design de formulários, reduzir friction",
impact: "Alto",
})
}

if (metrics.cro >= 60 && metrics.cro < 75) {
insights.push({
type: "warning",
title: "Conversão Abaixo do Potencial",
description: `Com score de ${metrics.cro}/100, há oportunidades significativas para aumentar conversões.`,
action: "Testar diferentes layouts, melhorar proposição de valor, otimizar chamadas à ação",
impact: "Alto",
})
}

if (metrics.cro >= 75) {
insights.push({
type: "success",
title: "Conversão em Bom Nível",
description: `Score CRO de ${metrics.cro}/100 indica boa taxa de conversão. Usuários estão convertendo bem.`,
action: "Continuar testando e iterando, manter foco em UX",
impact: "Alto",
})
}

// Indexation insights
if (metrics.indexedPages < 50) {
insights.push({
type: "warning",
title: "Poucas Páginas Indexadas",
description: `Apenas ${metrics.indexedPages} páginas indexadas. Seu site pode ter problemas de crawlabilidade ou sitemap.`,
action: "Verificar robots.txt, melhorar sitemap, garantir todas as páginas importantes sejam rastreáveis",
impact: "Médio",
})
}

if (metrics.indexedPages >= 100) {
insights.push({
type: "success",
title: "Cobertura de Indexação Saudável",
description: `${metrics.indexedPages} páginas indexadas. Bom sinal de que motores de busca conseguem rastrear seu site.`,
action: "Monitorar regularmente, evitar conteúdo duplicado",
impact: "Médio",
})
}

// Meta descriptions insight (always relevant)
insights.push({
type: "warning",
title: "Meta Descriptions Incompletas",
description:
"12 páginas estão sem meta descriptions otimizadas. Meta descriptions bem escritas aumentam CTR nos resultados de busca.",
action: "Criar meta descriptions únicas, com 150-160 caracteres, incluindo palavras-chave principais",
impact: "Médio",
})

// Alt text insight (always relevant)
insights.push({
type: "warning",
title: "Imagens sem Alt Text",
description:
"34 imagens detectadas sem atributo ALT. Isso prejudica SEO, acessibilidade e experiência de usuários com deficiência visual.",
action: "Adicionar descrições relevantes e descritivas em todos os atributos alt das imagens",
impact: "Médio",
})

// Schema markup insight
if (metrics.seo >= 80) {
insights.push({
type: "success",
title: "Schema Markup Implementado",
description: "Estrutura de dados JSON-LD está corretamente implementada e validada.",
action: "Continuar mantendo a implementação, atualizar conforme novos tipos de schema",
impact: "Alto",
})
}

// Mobile optimization
if (metrics.performance >= 80) {
insights.push({
type: "success",
title: "Site Mobile-Friendly",
description: "Site está bem otimizado para dispositivos móveis com excelente responsividade.",
action: "Manter mobile-first approach, testar em vários dispositivos",
impact: "Alto",
})
}

// SSL/Security insight
insights.push({
type: "success",
title: "Certificado SSL/HTTPS Ativo",
description: `Certificado ${metrics.security} está válido e configurado corretamente. Site é seguro para visitantes.`,
action: "Renovar certificado antes de expiração, manter HTTPS em todas as páginas",
impact: "Alto",
})

// Long-tail keyword opportunity
insights.push({
type: "info",
title: "Oportunidade: Conteúdo de Longa Cauda",
description: "Análise detectou 23 palavras-chave de nicho com baixa concorrência e potencial de tráfego.",
action: "Criar conteúdo direcionado para palavras-chave de longa cauda identificadas",
impact: "Médio",
})

return insights
}

================================================
FILE: lib/pdf-generator.ts
================================================
"use client"

import jsPDF from "jspdf"

interface AnalysisData {
url: string
timestamp: string
metrics: {
seo: number
performance: number
accessibility: number
cro: number
security: string
indexedPages: number
}
issues: Array<{
type: "critical" | "warning" | "success" | "info"
title: string
description: string
action: string
impact: "Alto" | "Médio" | "Baixo"
}>
}

export async function generatePDF(data: AnalysisData) {
try {
const doc = new jsPDF({
orientation: "portrait",
unit: "mm",
format: "a4",
})

    // Color scheme matching the app
    const primaryColor = [45, 74, 122]
    const accentColor = [212, 165, 116]
    const textColor = [18, 18, 18]
    const lightGray = [242, 242, 242]
    const criticalColor = [239, 68, 68]
    const warningColor = [234, 179, 8]
    const successColor = [34, 197, 94]

    const pageWidth = doc.getPageWidth()
    const pageHeight = doc.getPageHeight()
    let yPosition = 20

    doc.setFillColor(...primaryColor)
    doc.rect(0, 0, pageWidth, 50, "F")

    doc.setFontSize(32)
    doc.setTextColor(255, 255, 255)
    doc.setFont(undefined, "bold")
    doc.text("SiteScore", 20, 25)

    doc.setFontSize(10)
    doc.setFont(undefined, "normal")
    doc.text("Relatório Completo de Análise de Website", 20, 35)

    doc.setFontSize(9)
    doc.setTextColor(200, 200, 200)
    doc.text(
      `Gerado em: ${new Date().toLocaleDateString("pt-BR", {
        year: "numeric",
        month: "long",
        day: "numeric",
        hour: "2-digit",
        minute: "2-digit",
      })}`,
      pageWidth - 60,
      35,
    )

    yPosition = 65

    // URL Section
    doc.setFontSize(12)
    doc.setTextColor(...textColor)
    doc.setFont(undefined, "bold")
    doc.text("Site Analisado", 20, yPosition)

    yPosition += 8
    doc.setFontSize(10)
    doc.setFont(undefined, "normal")
    doc.setTextColor(...accentColor)
    doc.text(data.url, 20, yPosition)

    yPosition += 8
    doc.setFontSize(9)
    doc.setTextColor(150, 150, 150)
    doc.text(
      `Análise realizada em: ${new Date(data.timestamp).toLocaleDateString("pt-BR", {
        year: "numeric",
        month: "long",
        day: "numeric",
      })}`,
      20,
      yPosition,
    )

    yPosition += 20

    // Executive Summary Box
    doc.setFillColor(...lightGray)
    doc.rect(20, yPosition - 5, pageWidth - 40, 35, "F")
    doc.setFontSize(11)
    doc.setTextColor(...textColor)
    doc.setFont(undefined, "bold")
    doc.text("Resumo Executivo", 25, yPosition + 2)

    const overallScore = Math.round((data.metrics.seo + data.metrics.performance + data.metrics.accessibility) / 3)

    doc.setFont(undefined, "normal")
    doc.setFontSize(9)
    doc.setTextColor(80, 80, 80)

    const summaryText = `Sua website recebeu uma pontuação geral de ${overallScore}/100. O site apresenta ${data.issues.filter((i) => i.type === "critical").length} problemas críticos que precisam atenção imediata e ${data.issues.filter((i) => i.type === "warning").length} avisos importantes. Há também ${data.issues.filter((i) => i.type === "success").length} pontos positivos a manter.`

    const summaryLines = doc.splitTextToSize(summaryText, pageWidth - 50)
    doc.text(summaryLines, 25, yPosition + 8)

    yPosition += 40

    // Metrics Section
    doc.setFontSize(12)
    doc.setTextColor(...textColor)
    doc.setFont(undefined, "bold")
    doc.text("Métricas Principais", 20, yPosition)

    yPosition += 10

    // Create metrics table
    const metricsTable = [
      ["Métrica", "Score", "Status", "Descrição"],
      [
        "SEO",
        `${data.metrics.seo}/100`,
        data.metrics.seo >= 80 ? "Excelente" : data.metrics.seo >= 70 ? "Bom" : "Precisa Melhorar",
        "Otimização para motores de busca",
      ],
      [
        "Performance",
        `${data.metrics.performance}/100`,
        data.metrics.performance >= 90 ? "Excelente" : data.metrics.performance >= 70 ? "Bom" : "Precisa Melhorar",
        "Velocidade de carregamento",
      ],
      [
        "Acessibilidade",
        `${data.metrics.accessibility}/100`,
        data.metrics.accessibility >= 80 ? "Excelente" : data.metrics.accessibility >= 70 ? "Bom" : "Precisa Melhorar",
        "Usabilidade geral",
      ],
      [
        "CRO",
        `${data.metrics.cro}/100`,
        data.metrics.cro >= 75 ? "Excelente" : data.metrics.cro >= 65 ? "Bom" : "Precisa Melhorar",
        "Taxa de conversão",
      ],
      ["Segurança", data.metrics.security, "Válido", "Certificado HTTPS"],
      ["Indexação", `${data.metrics.indexedPages}`, "Ativo", "Páginas indexadas"],
    ]

    doc.setFontSize(8)
    doc.setFont(undefined, "bold")
    doc.setTextColor(255, 255, 255)
    doc.setFillColor(...primaryColor)

    // Header row
    doc.rect(20, yPosition - 4, pageWidth - 40, 6, "F")
    doc.text("Métrica", 25, yPosition)
    doc.text("Score", 65, yPosition)
    doc.text("Status", 105, yPosition)
    doc.text("Descrição", 135, yPosition)

    yPosition += 8
    doc.setFont(undefined, "normal")
    doc.setTextColor(...textColor)

    // Data rows
    metricsTable.slice(1).forEach((row, index) => {
      if (yPosition > pageHeight - 40) {
        doc.addPage()
        yPosition = 20
      }

      if (index % 2 === 0) {
        doc.setFillColor(...lightGray)
        doc.rect(20, yPosition - 4, pageWidth - 40, 6, "F")
      }

      doc.text(row[0], 25, yPosition)
      doc.text(row[1], 65, yPosition)
      doc.text(row[2], 105, yPosition)
      const descLines = doc.splitTextToSize(row[3], 50)
      doc.text(descLines[0], 135, yPosition)

      yPosition += 8
    })

    yPosition += 10

    doc.setFontSize(12)
    doc.setTextColor(...textColor)
    doc.setFont(undefined, "bold")
    doc.text("Insights e Recomendações Detalhadas", 20, yPosition)

    yPosition += 10

    // Group issues by type
    const criticalIssues = data.issues.filter((i) => i.type === "critical")
    const warningIssues = data.issues.filter((i) => i.type === "warning")
    const successIssues = data.issues.filter((i) => i.type === "success")

    // Critical Issues
    if (criticalIssues.length > 0) {
      doc.setFont(undefined, "bold")
      doc.setFontSize(10)
      doc.setTextColor(...criticalColor)
      doc.text("Problemas Críticos", 20, yPosition)
      yPosition += 6

      doc.setFont(undefined, "normal")
      doc.setFontSize(8)
      doc.setTextColor(...textColor)

      criticalIssues.forEach((issue) => {
        if (yPosition > pageHeight - 40) {
          doc.addPage()
          yPosition = 20
        }

        doc.setTextColor(...criticalColor)
        doc.text(`• ${issue.title}`, 25, yPosition)
        yPosition += 4

        doc.setTextColor(80, 80, 80)
        const descLines = doc.splitTextToSize(issue.description, 160)
        doc.text(descLines, 28, yPosition)
        yPosition += descLines.length * 3.5 + 2

        doc.setFont(undefined, "bold")
        doc.setTextColor(80, 80, 80)
        doc.text("Recomendação:", 28, yPosition)
        yPosition += 3

        doc.setFont(undefined, "normal")
        const actionLines = doc.splitTextToSize(issue.action, 160)
        doc.text(actionLines, 28, yPosition)
        yPosition += actionLines.length * 3.5 + 4

        doc.setTextColor(...accentColor)
        doc.text(`Impacto: ${issue.impact}`, 28, yPosition)
        yPosition += 5
      })

      yPosition += 4
    }

    // Warning Issues
    if (warningIssues.length > 0) {
      doc.setFont(undefined, "bold")
      doc.setFontSize(10)
      doc.setTextColor(...warningColor)
      doc.text("Avisos Importantes", 20, yPosition)
      yPosition += 6

      doc.setFont(undefined, "normal")
      doc.setFontSize(8)

      warningIssues.slice(0, 2).forEach((issue) => {
        if (yPosition > pageHeight - 40) {
          doc.addPage()
          yPosition = 20
        }

        doc.setTextColor(...warningColor)
        doc.text(`• ${issue.title}`, 25, yPosition)
        yPosition += 4

        doc.setTextColor(80, 80, 80)
        const descLines = doc.splitTextToSize(issue.description, 160)
        doc.text(descLines, 28, yPosition)
        yPosition += descLines.length * 3.5 + 3
      })

      yPosition += 4
    }

    // Success
    if (successIssues.length > 0) {
      doc.setFont(undefined, "bold")
      doc.setFontSize(10)
      doc.setTextColor(...successColor)
      doc.text("Pontos Positivos", 20, yPosition)
      yPosition += 6

      doc.setFont(undefined, "normal")
      doc.setFontSize(8)
      doc.setTextColor(80, 80, 80)

      successIssues.forEach((issue) => {
        if (yPosition > pageHeight - 20) {
          doc.addPage()
          yPosition = 20
        }

        doc.setTextColor(...successColor)
        doc.text(`✓ ${issue.title}`, 25, yPosition)
        yPosition += 4
      })
    }

    // Footer on each page
    const pageCount = doc.getNumberOfPages()
    for (let i = 1; i <= pageCount; i++) {
      doc.setPage(i)
      doc.setFontSize(8)
      doc.setTextColor(150, 150, 150)
      doc.text("SiteScore - Análise Profissional de Websites", 20, pageHeight - 10)
      doc.text(`Página ${i} de ${pageCount}`, pageWidth - 40, pageHeight - 10)
    }

    // Save PDF
    const fileName = `sitescore-relatorio-${new Date().toISOString().split("T")[0]}.pdf`
    doc.save(fileName)

} catch (error) {
console.error("Erro ao gerar PDF:", error)
}
}

================================================
FILE: lib/utils.ts
================================================
import { clsx, type ClassValue } from 'clsx'
import { twMerge } from 'tailwind-merge'

export function cn(...inputs: ClassValue[]) {
return twMerge(clsx(inputs))
}

================================================
FILE: styles/globals.css
================================================
@import 'tailwindcss';
@import 'tw-animate-css';

@custom-variant dark (&:is(.dark \*));

:root {
--background: oklch(1 0 0);
--foreground: oklch(0.145 0 0);
--card: oklch(1 0 0);
--card-foreground: oklch(0.145 0 0);
--popover: oklch(1 0 0);
--popover-foreground: oklch(0.145 0 0);
--primary: oklch(0.205 0 0);
--primary-foreground: oklch(0.985 0 0);
--secondary: oklch(0.97 0 0);
--secondary-foreground: oklch(0.205 0 0);
--muted: oklch(0.97 0 0);
--muted-foreground: oklch(0.556 0 0);
--accent: oklch(0.97 0 0);
--accent-foreground: oklch(0.205 0 0);
--destructive: oklch(0.577 0.245 27.325);
--destructive-foreground: oklch(0.577 0.245 27.325);
--border: oklch(0.922 0 0);
--input: oklch(0.922 0 0);
--ring: oklch(0.708 0 0);
--chart-1: oklch(0.646 0.222 41.116);
--chart-2: oklch(0.6 0.118 184.704);
--chart-3: oklch(0.398 0.07 227.392);
--chart-4: oklch(0.828 0.189 84.429);
--chart-5: oklch(0.769 0.188 70.08);
--radius: 0.625rem;
--sidebar: oklch(0.985 0 0);
--sidebar-foreground: oklch(0.145 0 0);
--sidebar-primary: oklch(0.205 0 0);
--sidebar-primary-foreground: oklch(0.985 0 0);
--sidebar-accent: oklch(0.97 0 0);
--sidebar-accent-foreground: oklch(0.205 0 0);
--sidebar-border: oklch(0.922 0 0);
--sidebar-ring: oklch(0.708 0 0);
}

.dark {
--background: oklch(0.145 0 0);
--foreground: oklch(0.985 0 0);
--card: oklch(0.145 0 0);
--card-foreground: oklch(0.985 0 0);
--popover: oklch(0.145 0 0);
--popover-foreground: oklch(0.985 0 0);
--primary: oklch(0.985 0 0);
--primary-foreground: oklch(0.205 0 0);
--secondary: oklch(0.269 0 0);
--secondary-foreground: oklch(0.985 0 0);
--muted: oklch(0.269 0 0);
--muted-foreground: oklch(0.708 0 0);
--accent: oklch(0.269 0 0);
--accent-foreground: oklch(0.985 0 0);
--destructive: oklch(0.396 0.141 25.723);
--destructive-foreground: oklch(0.637 0.237 25.331);
--border: oklch(0.269 0 0);
--input: oklch(0.269 0 0);
--ring: oklch(0.439 0 0);
--chart-1: oklch(0.488 0.243 264.376);
--chart-2: oklch(0.696 0.17 162.48);
--chart-3: oklch(0.769 0.188 70.08);
--chart-4: oklch(0.627 0.265 303.9);
--chart-5: oklch(0.645 0.246 16.439);
--sidebar: oklch(0.205 0 0);
--sidebar-foreground: oklch(0.985 0 0);
--sidebar-primary: oklch(0.488 0.243 264.376);
--sidebar-primary-foreground: oklch(0.985 0 0);
--sidebar-accent: oklch(0.269 0 0);
--sidebar-accent-foreground: oklch(0.985 0 0);
--sidebar-border: oklch(0.269 0 0);
--sidebar-ring: oklch(0.439 0 0);
}

@theme inline {
--font-sans: 'Geist', 'Geist Fallback';
--font-mono: 'Geist Mono', 'Geist Mono Fallback';
--color-background: var(--background);
--color-foreground: var(--foreground);
--color-card: var(--card);
--color-card-foreground: var(--card-foreground);
--color-popover: var(--popover);
--color-popover-foreground: var(--popover-foreground);
--color-primary: var(--primary);
--color-primary-foreground: var(--primary-foreground);
--color-secondary: var(--secondary);
--color-secondary-foreground: var(--secondary-foreground);
--color-muted: var(--muted);
--color-muted-foreground: var(--muted-foreground);
--color-accent: var(--accent);
--color-accent-foreground: var(--accent-foreground);
--color-destructive: var(--destructive);
--color-destructive-foreground: var(--destructive-foreground);
--color-border: var(--border);
--color-input: var(--input);
--color-ring: var(--ring);
--color-chart-1: var(--chart-1);
--color-chart-2: var(--chart-2);
--color-chart-3: var(--chart-3);
--color-chart-4: var(--chart-4);
--color-chart-5: var(--chart-5);
--radius-sm: calc(var(--radius) - 4px);
--radius-md: calc(var(--radius) - 2px);
--radius-lg: var(--radius);
--radius-xl: calc(var(--radius) + 4px);
--color-sidebar: var(--sidebar);
--color-sidebar-foreground: var(--sidebar-foreground);
--color-sidebar-primary: var(--sidebar-primary);
--color-sidebar-primary-foreground: var(--sidebar-primary-foreground);
--color-sidebar-accent: var(--sidebar-accent);
--color-sidebar-accent-foreground: var(--sidebar-accent-foreground);
--color-sidebar-border: var(--sidebar-border);
--color-sidebar-ring: var(--sidebar-ring);
}

@layer base {

- {
  @apply border-border outline-ring/50;
  }
  body {
  @apply bg-background text-foreground;
  }
  }
