import { render, screen } from "@testing-library/react";
import React from "react";
import { describe, expect, it } from "vitest";

import Home from "../src/app/page";

describe("workspace shell", () => {
  it("renders the YuruAgent workspace entry point", () => {
    render(<Home />);

    expect(
      screen.getByRole("heading", { name: "YuruAgent Workspace" }),
    ).toBeInTheDocument();
    expect(screen.getAllByText("Agent Workspace").length).toBeGreaterThan(0);
    expect(screen.getAllByText("Run History").length).toBeGreaterThan(0);
    expect(screen.getAllByText("Settings").length).toBeGreaterThan(0);
  });
});
