import type { LucideIcon } from "lucide-react";
import React from "react";

type StatusCardProps = {
  title: string;
  description: string;
  phase: string;
  icon: LucideIcon;
};

export function StatusCard({ title, description, phase, icon: Icon }: StatusCardProps) {
  return (
    <article className="statusCard">
      <div className="statusHeader">
        <span className="moduleIcon" aria-hidden="true">
          <Icon size={20} />
        </span>
        <span className="phaseTag">{phase}</span>
      </div>
      <h2>{title}</h2>
      <p>{description}</p>
    </article>
  );
}
