import { Activity, Bot, Home, Settings } from "lucide-react";
import React from "react";
import type { ReactNode } from "react";

const navigation = [
  { label: "Overview", href: "/", icon: Home, active: true },
  { label: "Agent Workspace", href: "/agents", icon: Bot, active: false },
  { label: "Run History", href: "/runs", icon: Activity, active: false },
  { label: "Settings", href: "/settings", icon: Settings, active: false },
];

type WorkspaceShellProps = {
  children: ReactNode;
};

export function WorkspaceShell({ children }: WorkspaceShellProps) {
  return (
    <div className="workspaceShell">
      <aside className="sidebar" aria-label="Main navigation">
        <a className="brand" href="/">
          <span className="brandMark">Y</span>
          <span>YuruAgent</span>
        </a>
        <nav className="nav">
          {navigation.map((item) => (
            <a
              key={item.href}
              className={item.active ? "navItem active" : "navItem"}
              href={item.href}
              aria-current={item.active ? "page" : undefined}
            >
              <item.icon size={18} />
              <span>{item.label}</span>
            </a>
          ))}
        </nav>
      </aside>
      <main className="content">{children}</main>
    </div>
  );
}
