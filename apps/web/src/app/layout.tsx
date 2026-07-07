import type { Metadata } from "next";
import React from "react";
import type { ReactNode } from "react";

import "./styles.css";

export const metadata: Metadata = {
  title: "YuruAgent",
  description: "Personal automation agent workspace.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
