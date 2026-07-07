import { Activity, Bot, Database, Settings, Workflow } from "lucide-react";
import React from "react";

import { StatusCard } from "../components/status-card";
import { WorkspaceShell } from "../components/workspace-shell";

const modules = [
  {
    title: "Agent Workspace",
    description: "Reserved for creating agents, prompts, model defaults, and context toggles.",
    phase: "Phase 1",
    icon: Bot,
  },
  {
    title: "Run History",
    description: "Reserved for streamed runs, final outputs, errors, and historical review.",
    phase: "Phase 2",
    icon: Activity,
  },
  {
    title: "Memory and RAG",
    description: "Reserved for typed memory, document retrieval, and source traceability.",
    phase: "Phase 4-6",
    icon: Database,
  },
  {
    title: "Workflow Builder",
    description: "Reserved for graph nodes, branches, tool calls, and human approval steps.",
    phase: "Phase 8",
    icon: Workflow,
  },
];

export default function Home() {
  return (
    <WorkspaceShell>
      <section className="toolbar" aria-label="Workspace overview">
        <div>
          <p className="eyebrow">Project Foundation</p>
          <h1>YuruAgent Workspace</h1>
        </div>
        <a className="iconButton" href="/settings" aria-label="Settings">
          <Settings size={20} />
        </a>
      </section>

      <section className="statusGrid" aria-label="Reserved modules">
        {modules.map((module) => (
          <StatusCard
            key={module.title}
            title={module.title}
            description={module.description}
            phase={module.phase}
            icon={module.icon}
          />
        ))}
      </section>
    </WorkspaceShell>
  );
}
