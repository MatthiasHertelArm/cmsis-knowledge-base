// Kickoff deck v2: high level, diagram driven, data structure explained by real examples
const pptxgen = require("pptxgenjs");
const React = require("react");
const ReactDOMServer = require("react-dom/server");
const sharp = require("sharp");
const fa = require("react-icons/fa6");
const { applyTheme } = require("/root/.claude/skills/synced/f0e99fa7-7afd-479c-96f1-e22c15dbec15_17d29c85-b899-4802-a262-60705e4bd289/pptx/scripts/apply_theme.js");

const HEX = { ink: "0F2A33", teal: "137C80", copper: "C8692E", mist: "EEF4F4", white: "FFFFFF",
  slate: "4A5F66", sea: "5FA8A6", sand: "F3E3D6", berry: "9E3D5E", deep: "2F4F5A", line: "B7C9CC", muted: "7F959A" };
const THEME = { name: "CMSIS KB", headFontFace: "Arial", bodyFontFace: "Calibri",
  colors: { dk1: HEX.ink, lt1: HEX.white, dk2: HEX.slate, lt2: HEX.mist, accent1: HEX.teal, accent2: HEX.copper,
    accent3: HEX.sea, accent4: HEX.berry, accent5: HEX.deep, accent6: HEX.sand, hlink: HEX.teal, folHlink: HEX.slate } };

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";
pres.title = "CMSIS Knowledge Base: Team Kickoff";
pres.author = "Matthias Hertel";
pres.company = "Arm";
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
const C = pres.SchemeColor;
const W = 13.333, M = 0.6;

// node type colors (scheme)
const T = {
  entity: { fill: C.accent5, label: "Entity" },
  procedure: { fill: C.accent1, label: "Procedure" },
  rule: { fill: C.accent2, label: "Rule" },
  concept: { fill: C.accent3, label: "Concept" },
  troubleshooting: { fill: C.accent4, label: "Troubleshooting" },
  artifact: { fill: C.text2, label: "Artifact" },
  doc: { fill: C.text2, label: "DocSection" },
};

async function icon(Comp, hex, size = 256) {
  const svg = ReactDOMServer.renderToStaticMarkup(React.createElement(Comp, { color: "#" + hex, size: String(size) }));
  return "image/png;base64," + (await sharp(Buffer.from(svg)).resize(size, size).png().toBuffer()).toString("base64");
}

// ---------- layouts ----------
const footer = { text: { text: "CMSIS Knowledge Base  |  Team kickoff  |  Arm internal", options: { x: M, y: 7.0, w: 8, h: 0.3, fontSize: 10, color: C.text2, margin: 0 } } };
const slideNum = { x: W - M - 0.6, y: 7.0, w: 0.6, h: 0.3, fontSize: 10, color: C.text2, align: "right" };
pres.defineSlideMaster({ title: "DARK", background: { color: C.text1 }, objects: [
  { placeholder: { options: { name: "title", type: "title", align: "left", x: M, y: 2.2, w: 8.6, h: 1.7, fontFace: "Arial", fontSize: 44, bold: true, color: C.background1, valign: "bottom", margin: 0 }, text: "" } },
  { placeholder: { options: { name: "sub", type: "body", x: M, y: 4.05, w: 8.4, h: 1.0, fontSize: 20, color: C.accent3, valign: "top", margin: 0 }, text: "" } },
] });
pres.defineSlideMaster({ title: "SECTION", background: { color: C.accent1 }, objects: [
  { placeholder: { options: { name: "num", type: "body", x: M, y: 2.2, w: 3, h: 0.9, fontFace: "Arial", fontSize: 48, bold: true, color: C.accent6, margin: 0 }, text: "" } },
  { placeholder: { options: { name: "title", type: "title", align: "left", x: M, y: 3.1, w: 11, h: 1.0, fontFace: "Arial", fontSize: 40, bold: true, color: C.background1, margin: 0 }, text: "" } },
  { placeholder: { options: { name: "sub", type: "body", x: M, y: 4.15, w: 11, h: 0.8, fontSize: 18, color: C.background2, margin: 0 }, text: "" } },
] });
pres.defineSlideMaster({ title: "CONTENT", background: { color: C.background1 }, objects: [
  { placeholder: { options: { name: "title", type: "title", align: "left", x: M, y: 0.35, w: W - 2 * M, h: 0.8, fontFace: "Arial", fontSize: 28, bold: true, color: C.text1, valign: "middle", margin: 0 }, text: "" } },
  footer ], slideNumber: slideNum });
pres.defineSlideMaster({ title: "BACKUP", background: { color: C.background2 }, objects: [
  { placeholder: { options: { name: "title", type: "title", align: "left", x: M, y: 0.35, w: W - 2 * M - 1.5, h: 0.8, fontFace: "Arial", fontSize: 26, bold: true, color: C.text1, valign: "middle", margin: 0 }, text: "" } },
  { text: { text: "BACKUP", options: { x: W - M - 1.3, y: 0.53, w: 1.3, h: 0.44, fontSize: 11, bold: true, color: C.background1, fill: { color: C.accent2 }, align: "center", valign: "middle", charSpacing: 2 } } },
  footer ], slideNumber: slideNum });

// ---------- helpers ----------
const txt = (s, text, o) => s.addText(text, Object.assign({ isTextBox: true, margin: 0, valign: "top", fontSize: 16, color: C.text1 }, o));
const card = (s, x, y, w, h, fill, name) => s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, rectRadius: 0.1, fill: { color: fill }, line: { color: fill }, objectName: name });
async function badge(s, Comp, x, y, d, bg, fg, name) {
  s.addShape(pres.shapes.OVAL, { x, y, w: d, h: d, fill: { color: bg }, line: { color: bg }, objectName: name + " badge" });
  s.addImage({ data: await icon(Comp, fg), x: x + d * 0.25, y: y + d * 0.25, w: d * 0.5, h: d * 0.5, objectName: name + " icon", altText: name });
}
// graph node: colored pill with small type label and main label
function node(s, x, y, w, h, kind, label, opt = {}) {
  const t = T[kind];
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, rectRadius: 0.12, fill: { color: opt.light ? C.background1 : t.fill },
    line: { color: t.fill, width: opt.light ? 2 : 1 }, objectName: `node ${label}`,
    shadow: { type: "outer", color: "000000", opacity: 0.15, blur: 4, offset: 1.5, angle: 90 } });
  const fg = opt.light ? t.fill : C.background1;
  txt(s, (opt.type || t.label).toUpperCase(), { x: x + 0.1, y: y + 0.08, w: w - 0.2, h: 0.25, fontSize: 9, bold: true, charSpacing: 1.5, color: opt.light ? t.fill : C.accent6, align: "center" });
  txt(s, label, { x: x + 0.1, y: y + 0.3, w: w - 0.2, h: h - 0.38, fontSize: opt.fs || 13, bold: true, color: opt.light ? C.text1 : fg, align: "center", valign: "middle", fontFace: opt.mono ? "Courier New" : undefined });
}
// arrow from (x1,y1) to (x2,y2), optional label at midpoint
function arrow(s, x1, y1, x2, y2, label, opt = {}) {
  const w = Math.abs(x2 - x1), h = Math.abs(y2 - y1);
  s.addShape(pres.shapes.LINE, { x: Math.min(x1, x2), y: Math.min(y1, y2), w: Math.max(w, 0.001), h: Math.max(h, 0.001),
    flipH: x2 < x1, flipV: y2 < y1, line: { color: opt.color || C.text2, width: 1.5, endArrowType: "triangle", dashType: opt.dash || "solid" }, objectName: "edge " + (label || "") });
  if (label) {
    const lw = opt.lw || 1.4;
    txt(s, label, { x: (x1 + x2) / 2 - lw / 2 + (opt.dx || 0), y: (y1 + y2) / 2 - 0.16 + (opt.dy || 0), w: lw, h: 0.3, fontSize: 11, italic: true, color: C.text2, align: "center", valign: "middle", fill: { color: opt.bg || C.background1 } });
  }
}
function content(sec, title) { const s = pres.addSlide({ masterName: "CONTENT", sectionTitle: sec }); s.addText(title, { placeholder: "title" }); return s; }
function backup(title) { const s = pres.addSlide({ masterName: "BACKUP", sectionTitle: "Backup" }); s.addText(title, { placeholder: "title" }); return s; }
function section(num, title, sub) {
  pres.addSection({ title });
  const s = pres.addSlide({ masterName: "SECTION", sectionTitle: title });
  s.addText(num, { placeholder: "num" }); s.addText(title, { placeholder: "title" }); s.addText(sub, { placeholder: "sub" });
  return s;
}
function legend(s, kinds, y = 6.45) {
  let x = M;
  for (const k of kinds) {
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: y + 0.06, w: 0.32, h: 0.2, rectRadius: 0.05, fill: { color: T[k].fill }, line: { color: T[k].fill }, objectName: "legend " + k });
    txt(s, T[k].label, { x: x + 0.4, y, w: 1.6, h: 0.32, fontSize: 12, color: C.text2, valign: "middle" });
    x += 0.4 + T[k].label.length * 0.085 + 0.45;
  }
}
const chartText = { catAxisLabelFontFace: "+mn-lt", valAxisLabelFontFace: "+mn-lt", dataLabelFontFace: "+mn-lt", titleFontFace: "+mn-lt", legendFontFace: "+mn-lt" };

(async () => {
  // ================= Opening =================
  pres.addSection({ title: "Opening" });
  let s = pres.addSlide({ masterName: "DARK", sectionTitle: "Opening" });
  s.addText("CMSIS Knowledge Base", { placeholder: "title" });
  s.addText("Team kickoff: giving the CMSIS Developer Assistant the know-how that Pack Docs don't have", { placeholder: "sub" });
  txt(s, "Embedded Tools Integration  |  October 2026", { x: M, y: 6.4, w: 8, h: 0.4, fontSize: 12, color: C.accent3 });
  // decorative mini graph in brand colors
  const g = [[10.2, 1.6, "procedure"], [11.9, 2.6, "rule"], [10.0, 3.6, "entity"], [11.6, 4.5, "concept"], [10.6, 5.3, "troubleshooting"]];
  const cx = (p) => p[0] + 0.35, cy = (p) => p[1] + 0.35;
  [[0, 1], [0, 2], [2, 3], [1, 3], [2, 4], [3, 4]].forEach(([a, b]) => s.addShape(pres.shapes.LINE, { x: Math.min(cx(g[a]), cx(g[b])), y: Math.min(cy(g[a]), cy(g[b])), w: Math.abs(cx(g[a]) - cx(g[b])) || 0.001, h: Math.abs(cy(g[a]) - cy(g[b])) || 0.001, flipH: (cx(g[b]) < cx(g[a])) !== (cy(g[b]) < cy(g[a])), line: { color: C.text2, width: 2 }, objectName: "motif edge" }));
  g.forEach((p) => s.addShape(pres.shapes.OVAL, { x: p[0], y: p[1], w: 0.7, h: 0.7, fill: { color: T[p[2]].fill }, line: { color: C.text1, width: 3 }, objectName: "motif node" }));
  s.addNotes("Goal: align on the idea, see how the data looks, agree on pilot domain and owners.");

  // 2 The one idea
  s = content("Opening", "Pack Docs say what exists. We add how, when and why");
  const cols = [
    [fa.FaBook, "WHAT", "Pack Docs", "APIs, parameters, device facts, datasheets. Already in the CDA.", C.text2, HEX.slate],
    [fa.FaListCheck, "HOW", "Procedures", "Step by step workflows with checks and stop points.", C.accent1, HEX.teal],
    [fa.FaClock, "WHEN", "Rules and patterns", "Constraints, trade-offs, what wins in which context.", C.accent2, HEX.copper],
    [fa.FaCircleQuestion, "WHY", "Troubleshooting", "Exact error text, cause and fix.", C.accent4, HEX.berry],
  ];
  for (let i = 0; i < 4; i++) {
    const x = M + i * 3.07;
    card(s, x, 1.5, 2.85, 4.0, C.background2, "col " + i);
    await badge(s, cols[i][0], x + 0.95, 1.8, 0.95, cols[i][5], HEX.white, cols[i][1]);
    txt(s, cols[i][1], { x: x + 0.2, y: 2.95, w: 2.45, h: 0.5, fontSize: 24, bold: true, fontFace: "Arial", color: cols[i][4], align: "center" });
    txt(s, cols[i][2], { x: x + 0.2, y: 3.5, w: 2.45, h: 0.4, fontSize: 17, bold: true, align: "center" });
    txt(s, cols[i][3], { x: x + 0.25, y: 4.0, w: 2.35, h: 1.3, fontSize: 14, color: C.text2, align: "center" });
  }
  txt(s, [{ text: "Glue: ", options: { bold: true, color: C.accent1 } }, { text: "both sides point at the same CMSIS entities (device, core, component, toolchain). The agent's project context selects what applies.", options: {} }],
    { x: M, y: 5.8, w: W - 2 * M, h: 0.7, fontSize: 17, valign: "middle" });

  // 3 Problem today
  s = content("Opening", "Why skills alone don't scale");
  const prob = [
    [fa.FaFileLines, "All or nothing", "24 skills, ~36k tokens. A skill is loaded whole or not at all.", "36k"],
    [fa.FaMicrochip, "Blind to the project", "Skills are picked by their description, not by the device, components or compiler in cbuild.yml.", "24"],
    [fa.FaFeather, "Too heavy for small models", "On-device models need short summaries first, detail on request.", "~500"],
  ];
  const big = ["tokens in all skills", "skills chosen by description only", "tokens per KB search"];
  for (let i = 0; i < 3; i++) {
    const x = M + i * 4.1;
    card(s, x, 1.5, 3.85, 4.9, i === 2 ? C.text1 : C.background2, "prob " + i);
    const dark = i === 2;
    await badge(s, prob[i][0], x + 0.3, 1.8, 0.8, dark ? HEX.copper : HEX.teal, HEX.white, prob[i][1]);
    txt(s, prob[i][1], { x: x + 0.3, y: 2.8, w: 3.3, h: 0.5, fontSize: 19, bold: true, color: dark ? C.background1 : C.text1 });
    txt(s, prob[i][2], { x: x + 0.3, y: 3.35, w: 3.3, h: 1.0, fontSize: 15, color: dark ? C.background2 : C.text2 });
    txt(s, prob[i][3], { x: x + 0.3, y: 4.55, w: 3.3, h: 0.95, fontSize: 48, bold: true, fontFace: "Arial", color: dark ? C.accent6 : C.accent1 });
    txt(s, big[i], { x: x + 0.3, y: 5.5, w: 3.3, h: 0.4, fontSize: 13, color: dark ? C.background2 : C.text2 });
  }
  txt(s, "The third card is the target: what the prototype returns per search today.", { x: M, y: 6.5, w: W - 2 * M, h: 0.35, fontSize: 12, italic: true, color: C.text2 });

  // 4 Big picture diagram
  s = content("Opening", "The big picture");
  // sources column
  const srcs = [["Pack index + PDSC", fa.FaBoxesStacked], ["cmsis-skills", fa.FaScrewdriverWrench], ["devtools messages", fa.FaTerminal], ["Docs and guides", fa.FaBookOpen]];
  for (let i = 0; i < srcs.length; i++) {
    const y = 1.45 + i * 1.22;
    card(s, M, y, 2.9, 1.0, C.background2, "src " + i);
    await badge(s, srcs[i][1], M + 0.15, y + 0.17, 0.66, HEX.slate, HEX.white, srcs[i][0]);
    txt(s, srcs[i][0], { x: M + 0.95, y: y + 0.1, w: 1.85, h: 0.8, fontSize: 14, bold: true, valign: "middle" });
    arrow(s, M + 2.95, y + 0.5, 4.55, 3.4 + (i - 1.5) * 0.35);
  }
  // central store
  card(s, 4.6, 1.45, 4.2, 4.65, C.text1, "kb store");
  txt(s, "Knowledge base", { x: 4.85, y: 1.6, w: 3.7, h: 0.45, fontSize: 19, bold: true, color: C.background1, align: "center" });
  txt(s, "Git: Markdown units  →  CI  →  one SQLite file", { x: 4.85, y: 2.05, w: 3.7, h: 0.35, fontSize: 12, color: C.accent3, align: "center" });
  // mini graph inside
  const mg = [[5.2, 2.75, "entity"], [6.4, 2.6, "procedure"], [7.6, 2.85, "rule"], [5.6, 3.95, "concept"], [7.0, 4.0, "troubleshooting"], [6.3, 5.0, "entity"]];
  const mcx = (p) => p[0] + 0.3, mcy = (p) => p[1] + 0.3;
  [[0, 1], [1, 2], [1, 3], [3, 4], [4, 5], [0, 5], [2, 4]].forEach(([a, b]) => s.addShape(pres.shapes.LINE, { x: Math.min(mcx(mg[a]), mcx(mg[b])), y: Math.min(mcy(mg[a]), mcy(mg[b])), w: Math.abs(mcx(mg[a]) - mcx(mg[b])) || 0.001, h: Math.abs(mcy(mg[a]) - mcy(mg[b])) || 0.001, flipH: (mcx(mg[b]) < mcx(mg[a])) !== (mcy(mg[b]) < mcy(mg[a])), line: { color: C.text2, width: 1.5 }, objectName: "mini edge" }));
  mg.forEach((p) => s.addShape(pres.shapes.OVAL, { x: p[0], y: p[1], w: 0.6, h: 0.6, fill: { color: T[p[2]].fill }, line: { color: C.text1, width: 2 }, objectName: "mini node" }));
  // output
  arrow(s, 8.85, 3.75, 9.95, 3.75, "MCP", { lw: 0.6 });
  card(s, 10.0, 1.45, W - M - 10.0, 4.65, C.background2, "cda");
  await badge(s, fa.FaRobot, 10.0 + (W - M - 10.0) / 2 - 0.45, 1.75, 0.9, HEX.teal, HEX.white, "CDA agent");
  txt(s, "CDA agent", { x: 10.15, y: 2.75, w: W - M - 10.3, h: 0.4, fontSize: 17, bold: true, align: "center" });
  txt(s, [
    { text: "search", options: { fontFace: "Courier New", bold: true, color: C.accent1, breakLine: true } },
    { text: "find units for this project", options: { breakLine: true } },
    { text: " ", options: { fontSize: 6, breakLine: true } },
    { text: "get", options: { fontFace: "Courier New", bold: true, color: C.accent1, breakLine: true } },
    { text: "read one unit in full", options: { breakLine: true } },
    { text: " ", options: { fontSize: 6, breakLine: true } },
    { text: "expand", options: { fontFace: "Courier New", bold: true, color: C.accent1, breakLine: true } },
    { text: "follow the graph one hop", options: {} },
  ], { x: 10.2, y: 3.25, w: W - M - 10.4, h: 2.7, fontSize: 13, color: C.text2, align: "center" });
  txt(s, "Ships as a knowledge/ folder inside a CMSIS Pack. Vendors can add their own. No server, no graph DB, works offline.", { x: M, y: 6.35, w: W - 2 * M, h: 0.4, fontSize: 14, italic: true, color: C.text2 });

  // ================= Section: Data =================
  section("01", "How the data is structured", "Five real examples from the prototype");

  // 6 Two node classes
  s = content("How the data is structured", "Everything is a node. Two kinds of nodes");
  card(s, M, 1.45, 5.6, 4.75, C.background2, "entities card");
  await badge(s, fa.FaIndustry, M + 0.3, 1.7, 0.8, HEX.deep, HEX.white, "generated");
  txt(s, "Entities: generated", { x: M + 1.3, y: 1.75, w: 4.1, h: 0.45, fontSize: 20, bold: true });
  txt(s, "Built from the pack index and PDSC files. Nobody edits them.", { x: M + 1.3, y: 2.2, w: 4.1, h: 0.6, fontSize: 14, color: C.text2 });
  const ents = ["Pack", "Family", "Device", "Board", "Core", "Component", "API", "Toolchain"];
  ents.forEach((e, i) => {
    const x = M + 0.35 + (i % 4) * 1.27, y = 3.15 + Math.floor(i / 4) * 0.75;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w: 1.15, h: 0.55, rectRadius: 0.27, fill: { color: C.accent5 }, line: { color: C.accent5 }, objectName: "entity chip " + e });
    txt(s, e, { x, y, w: 1.15, h: 0.55, fontSize: 12, bold: true, color: C.background1, align: "center", valign: "middle" });
  });
  txt(s, "26,903 entities today", { x: M + 0.35, y: 4.85, w: 5, h: 0.6, fontSize: 26, bold: true, fontFace: "Arial", color: C.accent5 });
  txt(s, "They are the join keys to Pack Docs and to the user's project.", { x: M + 0.35, y: 5.45, w: 5, h: 0.5, fontSize: 14, color: C.text2 });

  card(s, M + 5.95, 1.45, W - 2 * M - 5.95, 4.75, C.background2, "units card");
  await badge(s, fa.FaPenNib, M + 6.25, 1.7, 0.8, HEX.teal, HEX.white, "curated");
  txt(s, "Knowledge units: curated", { x: M + 7.25, y: 1.75, w: 4.4, h: 0.45, fontSize: 20, bold: true });
  txt(s, "One Markdown file each, in Git, reviewed by a domain owner.", { x: M + 7.25, y: 2.2, w: 4.4, h: 0.6, fontSize: 14, color: C.text2 });
  const kinds = [["procedure", "How to do it"], ["rule", "Must or should"], ["concept", "What it means"], ["troubleshooting", "Error, cause, fix"]];
  kinds.forEach((k, i) => {
    const y = 3.05 + i * 0.75;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: M + 6.3, y, w: 2.2, h: 0.55, rectRadius: 0.27, fill: { color: T[k[0]].fill }, line: { color: T[k[0]].fill }, objectName: "unit chip " + k[0] });
    txt(s, T[k[0]].label, { x: M + 6.3, y, w: 2.2, h: 0.55, fontSize: 13, bold: true, color: C.background1, align: "center", valign: "middle" });
    txt(s, k[1], { x: M + 8.7, y, w: 3.0, h: 0.55, fontSize: 15, color: C.text1, valign: "middle" });
  });
  txt(s, "Edges connect them: part_of, applies_to, requires, constrains, refines.", { x: M, y: 6.4, w: W - 2 * M, h: 0.4, fontSize: 14, italic: true, color: C.text2 });

  // 7 Example 1: entity chain
  s = content("How the data is structured", "Example 1: one device and everything around it");
  const ny = 2.3, nw = 2.0, nh = 0.95, step = 2.53;
  const xs = [0, 1, 2, 3, 4].map((i) => M + i * step);
  node(s, xs[0], ny, nw, nh, "entity", "B-U585I-IOT02A", { type: "Board" });
  node(s, xs[1], ny, nw, nh, "entity", "STM32U585AIIx", { type: "Device" });
  node(s, xs[2], ny, nw, nh, "entity", "STM32U585", { type: "Subfamily" });
  node(s, xs[3], ny, nw, nh, "entity", "STM32U5 Series", { type: "Family" });
  node(s, xs[4], ny, nw, nh, "entity", "Keil::STM32U5xx_DFP", { type: "Pack", fs: 12 });
  arrow(s, xs[0] + nw, ny + nh / 2, xs[1], ny + nh / 2, "mounted_on", { dy: -0.72, lw: 1.1 });
  for (let i = 1; i < 4; i++) arrow(s, xs[i] + nw, ny + nh / 2, xs[i + 1], ny + nh / 2, "part_of", { dy: -0.72, lw: 0.9 });
  node(s, xs[1], 4.0, nw, nh, "entity", "Cortex-M33", { type: "Core" });
  arrow(s, xs[1] + nw / 2, ny + nh, xs[1] + nw / 2, 4.0, "has_core", { dx: 0.65, lw: 0.9 });
  node(s, xs[0], 4.0, nw, nh, "entity", "Keil::B-U585I-IOT02A_BSP", { type: "Pack", fs: 11 });
  arrow(s, xs[0] + nw / 2, ny + nh, xs[0] + nw / 2, 4.0, "part_of", { dx: 0.6, lw: 0.8 });
  // the payoff box
  card(s, xs[2], 3.95, W - M - xs[2], 1.95, C.background2, "payoff");
  txt(s, "Why it matters", { x: xs[2] + 0.25, y: 4.1, w: 6, h: 0.4, fontSize: 16, bold: true, color: C.accent1 });
  txt(s, [
    { text: "A unit tagged for the STM32U5 Series is valid for every device below it.", options: { bullet: true, breakLine: true } },
    { text: "A unit tagged Cortex-M33 reaches this device through has_core.", options: { bullet: true, breakLine: true } },
    { text: "Pack update removes a target? CI flags every unit that pointed at it.", options: { bullet: true } },
  ], { x: xs[2] + 0.25, y: 4.55, w: W - M - xs[2] - 0.5, h: 1.3, fontSize: 14, paraSpaceAfter: 4 });
  txt(s, [{ text: "Real data, generated from the STM32U5 DFP and B-U585I-IOT02A BSP.  ID format: ", options: {} }, { text: "device:STM32U585AIIx", options: { fontFace: "Courier New" } }],
    { x: M, y: 6.25, w: W - 2 * M, h: 0.35, fontSize: 12, italic: true, color: C.text2 });

  // 8 Example 2: anatomy of a unit
  s = content("How the data is structured", "Example 2: anatomy of one knowledge unit");
  card(s, M, 1.4, 7.3, 5.3, C.text1, "file card");
  txt(s, "ts-packchk-m302.md", { x: M + 0.3, y: 1.55, w: 5, h: 0.35, fontSize: 13, bold: true, color: C.accent3, fontFace: "Courier New" });
  const lines = [
    ["---", 0], ["id: ts-packchk-m302", 1], ["type: troubleshooting", 1], ["domain: error-catalog", 0],
    ["symptoms:", 2], ["  - \"M302\"", 2], ["  - \"No vendor tag found in the PDSC file...\"", 2],
    ["applies_to: { tool: [packchk] }", 3], ["status: draft", 4], ["source: devtools@30f5e81 packchk/README.md", 4], ["license: Apache-2.0   mode: V", 4], ["---", 0],
    ["## Cause", 5], ["Vendor name is mandatory ... Within <package>", 5], ["add <vendor>Keil</vendor>.", 5],
  ];
  const lc = [null, C.background1, C.accent6, C.accent3, C.background2, C.background1];
  lines.forEach((l, i) => txt(s, l[0], { x: M + 0.75, y: 2.0 + i * 0.3, w: 6.4, h: 0.3, fontSize: 12, fontFace: "Courier New", color: l[1] ? lc[l[1]] : C.text2, valign: "middle" }));
  const marks = [[1, 1.5], [2, 4.4], [3, 7], [4, 8.9], [5, 12.9]];
  marks.forEach(([n, li]) => {
    s.addShape(pres.shapes.OVAL, { x: M + 0.25, y: 2.0 + li * 0.3, w: 0.32, h: 0.32, fill: { color: C.accent2 }, line: { color: C.accent2 }, objectName: "marker " + n });
    txt(s, String(n), { x: M + 0.25, y: 2.0 + li * 0.3, w: 0.32, h: 0.32, fontSize: 11, bold: true, color: C.background1, align: "center", valign: "middle" });
  });
  const expl = [
    ["What it is", "Stable id and one of five types."],
    ["How it is found", "Exact error text. A pasted message matches first."],
    ["Where it applies", "Points at an entity. Here: the packchk tool."],
    ["Where it comes from", "Source commit, license, mode. Draft until a domain owner reviews it."],
    ["The knowledge", "Plain Markdown body. Never shortened when retrieved."],
  ];
  expl.forEach((e, i) => {
    const y = 1.45 + i * 1.04;
    s.addShape(pres.shapes.OVAL, { x: M + 7.65, y: y + 0.05, w: 0.42, h: 0.42, fill: { color: C.accent2 }, line: { color: C.accent2 }, objectName: "expl marker " + i });
    txt(s, String(i + 1), { x: M + 7.65, y: y + 0.05, w: 0.42, h: 0.42, fontSize: 14, bold: true, color: C.background1, align: "center", valign: "middle" });
    txt(s, e[0], { x: M + 8.25, y, w: 3.9, h: 0.4, fontSize: 16, bold: true });
    txt(s, e[1], { x: M + 8.25, y: y + 0.4, w: 3.9, h: 0.6, fontSize: 13, color: C.text2 });
  });

  // 9 Example 3: a procedure in the graph
  s = content("How the data is structured", "Example 3: a skill becomes a node with explicit dependencies");
  const cxp = 4.85, cyp = 3.35, cw = 3.0, ch = 1.05;
  node(s, cxp, cyp, cw, ch, "procedure", "generate-debug-sequences", { fs: 14 });
  const req = [["concept", "debug-sequence-contract"], ["procedure", "debug-knowledge"], ["procedure", "validate-pdsc-sequence-xml"], ["procedure", "apply-confirmed-pdsc-proposal"]];
  req.forEach((r, i) => {
    const y = 1.4 + i * 1.22;
    node(s, 9.75, y, 2.95, 0.9, r[0], r[1], { fs: 12, light: true });
    arrow(s, cxp + cw, cyp + ch / 2, 9.75, y + 0.45, i === 0 ? "requires" : null, { dy: -0.55, lw: 0.9 });
  });
  const rls = [["rule", "No fabrication"], ["rule", "Portability"], ["rule", "Scope"], ["rule", "Critical blockers"]];
  rls.forEach((r, i) => {
    const y = 1.4 + i * 1.22;
    node(s, M, y, 2.6, 0.9, r[0], r[1], { fs: 13, light: true });
    arrow(s, M + 2.6, y + 0.45, cxp, cyp + ch / 2, i === 0 ? "constrains" : null, { dy: -0.55, lw: 1.0 });
  });
  node(s, cxp + 0.1, 1.4, 2.8, 0.85, "artifact", "<pdsc>-debug-knowledge.md", { fs: 11, light: true });
  arrow(s, cxp + cw / 2, 2.25, cxp + cw / 2, cyp, "consumes", { dx: 0.65, lw: 0.9 });
  node(s, cxp + 0.1, 5.15, 2.8, 0.85, "doc", "Debug Description spec", { fs: 12, light: true });
  arrow(s, cxp + cw / 2, cyp + ch, cxp + cw / 2, 5.15, "references", { dx: 0.7, lw: 1.0 });
  legend(s, ["procedure", "rule", "concept", "artifact"], 6.35);
  txt(s, "Real neighbourhood from cmsis-skills. Today it is prose in one SKILL.md.", { x: 7.2, y: 6.35, w: W - M - 7.2, h: 0.32, fontSize: 12, italic: true, color: C.text2, align: "right", valign: "middle" });

  // 10 Example 4: canonical rule + refines
  s = content("How the data is structured", "Example 4: one rule written once, refined per procedure");
  node(s, W / 2 - 2.0, 1.45, 4.0, 1.0, "rule", "rule-no-fabrication", { type: "Canonical rule", fs: 15, mono: true });
  txt(s, "Written once by a human. Appears in 23 of 24 skills today, each with its own wording.", { x: W / 2 - 4.5, y: 2.55, w: 9.0, h: 0.4, fontSize: 13, italic: true, color: C.text2, align: "center" });
  const ref = [
    ["generate-debug-sequences", "reset, unlock, authentication, boot, flash, processor-control, low-power ... behavior"],
    ["evaluate-ethos-u-variants", "Report only values read from Vela's summary CSV and console output."],
    ["add-cmsis-target", "board, device, pack, version, layer, connection, path ... or schema result"],
  ];
  ref.forEach((r, i) => {
    const x = M + i * 4.1, y = 3.6;
    card(s, x, y, 3.85, 2.55, C.background2, "refine " + i);
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: x + 0.25, y: y + 0.25, w: 3.35, h: 0.5, rectRadius: 0.1, fill: { color: C.background1 }, line: { color: C.accent2, width: 1.5 }, objectName: "refine head " + i });
    txt(s, r[0], { x: x + 0.25, y: y + 0.25, w: 3.35, h: 0.5, fontSize: 12, bold: true, fontFace: "Courier New", align: "center", valign: "middle", color: C.accent2 });
    txt(s, "Delta only:", { x: x + 0.3, y: y + 0.95, w: 3.3, h: 0.3, fontSize: 12, bold: true, color: C.text2 });
    txt(s, "“" + r[1] + "”", { x: x + 0.3, y: y + 1.25, w: 3.3, h: 1.2, fontSize: 13, italic: true });
    arrow(s, x + 1.92, y, W / 2 + (i - 1) * 1.2, 3.02, i === 1 ? "refines" : null, { dx: 0.5, lw: 0.8, color: C.accent2 });
  });
  txt(s, "Delta texts are verbatim Stage 2 output from the real skills.", { x: M, y: 6.35, w: W - 2 * M, h: 0.32, fontSize: 12, italic: true, color: C.text2 });

  // 11 Example 5: context decides
  s = content("How the data is structured", "Example 5: the project context decides what the agent sees");
  node(s, M, 1.5, 3.3, 1.0, "concept", "Stack sizing pattern", { type: "Pattern (generic)", fs: 14 });
  node(s, M, 3.6, 3.3, 1.2, "concept", "Stack sizing for Cortex-M55 + AC6", { type: "Pattern (specific)", fs: 13 });
  arrow(s, M + 1.65, 3.6, M + 1.65, 2.5, "refines", { dx: 0.55, lw: 0.75 });
  txt(s, [{ text: "applies_to:", options: { bold: true, breakLine: true } }, { text: "core: Cortex-M55", options: { breakLine: true } }, { text: "compiler: AC6 >= 6.20", options: {} }],
    { x: M, y: 4.95, w: 3.3, h: 0.9, fontSize: 12, fontFace: "Courier New", color: C.text2 });
  const proj = [
    ["Project A", "Alif Ensemble, M55_HE core, AC6", fa.FaCircleCheck, "Gets the specific M55 unit", C.accent1, HEX.teal],
    ["Project B", "STM32U585AIIx, Cortex-M33, GCC", fa.FaCircleCheck, "Gets the generic unit", C.accent5, HEX.deep],
  ];
  for (let i = 0; i < 2; i++) {
    const y = 1.5 + i * 2.45;
    card(s, 4.6, y, W - M - 4.6, 2.15, C.background2, "project " + i);
    await badge(s, fa.FaFileCode, 4.85, y + 0.3, 0.75, HEX.slate, HEX.white, proj[i][0]);
    txt(s, proj[i][0], { x: 5.8, y: y + 0.28, w: 3.0, h: 0.4, fontSize: 17, bold: true });
    txt(s, "cbuild.yml: " + proj[i][1], { x: 5.8, y: y + 0.7, w: 3.2, h: 0.75, fontSize: 13, color: C.text2 });
    arrow(s, 9.05, y + 1.05, 9.55, y + 1.05);
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 9.6, y: y + 0.45, w: W - M - 9.85, h: 1.25, rectRadius: 0.1, fill: { color: proj[i][4] }, line: { color: proj[i][4] }, objectName: "result " + i });
    txt(s, proj[i][3], { x: 9.75, y: y + 0.45, w: W - M - 10.15, h: 1.25, fontSize: 15, bold: true, color: C.background1, align: "center", valign: "middle" });
  }
  txt(s, "Illustrative units (these two are test fixtures). Device to core resolution and the refines rule are real and covered by tests.", { x: M, y: 6.35, w: W - 2 * M, h: 0.32, fontSize: 12, italic: true, color: C.text2 });

  // ================= Section: Agent =================
  section("02", "How the agent uses it", "Small answers first, full detail on demand");

  // 13 Funnel
  s = content("How the agent uses it", "From 550 units to the one that matters");
  const fun = [
    ["550", "units in the index", "all domains, all targets", 11.3],
    ["filter", "by project context", "device, components, compiler from cbuild.yml", 9.4],
    ["rank", "keywords + meaning", "BM25 and embeddings, exact error text wins", 7.5],
    ["~525", "tokens returned", "top 5 as id, title, summary", 5.6],
    ["1", "unit read in full", "knowledge_get, never shortened", 4.6],
  ];
  fun.forEach((f, i) => {
    const w = f[3], x = (W - w) / 2, y = 1.4 + i * 1.03;
    const fills = [C.accent5, C.text2, C.accent3, C.accent1, C.accent2];
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h: 0.88, rectRadius: 0.1, fill: { color: fills[i] }, line: { color: fills[i] }, objectName: "funnel " + i });
    txt(s, f[0], { x: x + 0.25, y, w: 1.3, h: 0.88, fontSize: 24, bold: true, fontFace: "Arial", color: C.background1, valign: "middle" });
    txt(s, [{ text: f[1], options: { bold: true, breakLine: true } }, { text: f[2], options: { fontSize: 12 } }], { x: x + 1.55, y: y + 0.05, w: w - 1.75, h: 0.8, fontSize: 15, color: C.background1, valign: "middle" });
  });
  txt(s, "Measured on the prototype: 57 ms average per search, CPU only. Tokens estimated as characters / 4.", { x: M, y: 6.6, w: W - 2 * M, h: 0.3, fontSize: 12, italic: true, color: C.text2, align: "center" });

  // 14 Walk-through
  s = content("How the agent uses it", "Walk-through: a developer pastes an error");
  const bub = (x, y, w, h, fill, fg, text, name, mono) => { card(s, x, y, w, h, fill, name); txt(s, text, { x: x + 0.3, y: y + 0.15, w: w - 0.6, h: h - 0.3, fontSize: 14, color: fg, valign: "middle", fontFace: mono ? "Courier New" : undefined }); };
  await badge(s, fa.FaUser, M, 1.45, 0.7, HEX.slate, HEX.white, "developer");
  bub(M + 0.9, 1.4, 6.6, 0.85, C.background2, C.text1, "csolution convert fails with: error csolution: board mounted device STM32U585AIIx not found. What now?", "dev bubble");
  await badge(s, fa.FaRobot, M, 2.65, 0.7, HEX.teal, HEX.white, "agent");
  bub(M + 0.9, 2.55, 6.6, 0.95, C.text1, C.background1, "knowledge_search(query = <error text>, cbuild = \"app.cbuild.yml\")", "call bubble", true);
  // result list
  card(s, M + 0.9, 3.75, 6.6, 2.35, C.background2, "results");
  const rs = [["ts-csolution-board-mounted-device", "exact match", true], ["ts-csolution-is-not-among-board-mounted-devices", "", false], ["ts-packchk-m346", "", false], ["ts-csolution-found-no-mounted-device", "", false]];
  rs.forEach((r, i) => {
    const y = 3.95 + i * 0.5;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: M + 1.1, y, w: 0.18, h: 0.34, rectRadius: 0.04, fill: { color: r[2] ? C.accent4 : C.text2 }, line: { color: r[2] ? C.accent4 : C.text2 }, objectName: "rank " + i });
    txt(s, r[0], { x: M + 1.45, y, w: 4.6, h: 0.34, fontSize: 12, fontFace: "Courier New", bold: r[2], valign: "middle", color: r[2] ? C.text1 : C.text2 });
    if (r[1]) txt(s, r[1], { x: M + 6.05, y, w: 1.3, h: 0.34, fontSize: 11, bold: true, color: C.accent4, valign: "middle" });
  });
  const ws = [["1", "Context", "Device, components and compiler come from cbuild.yml."], ["2", "Match", "The error text hits the troubleshooting unit directly."], ["3", "Read", "The agent calls knowledge_get for that one unit and answers with cause and fix."]];
  ws.forEach((w, i) => {
    const y = 1.45 + i * 1.6;
    s.addShape(pres.shapes.OVAL, { x: 8.55, y, w: 0.6, h: 0.6, fill: { color: C.accent1 }, line: { color: C.accent1 }, objectName: "step " + i });
    txt(s, w[0], { x: 8.55, y, w: 0.6, h: 0.6, fontSize: 18, bold: true, color: C.background1, align: "center", valign: "middle" });
    txt(s, w[1], { x: 9.35, y: y + 0.05, w: 3.3, h: 0.45, fontSize: 18, bold: true });
    txt(s, w[2], { x: 9.35, y: y + 0.5, w: 3.35, h: 0.9, fontSize: 14, color: C.text2 });
  });
  txt(s, "Error reproduced with CMSIS-Toolbox 2.12.0 (B-U585I-IOT02A board, STM32U5 DFP not loaded). Ranking is real prototype output.", { x: M, y: 6.35, w: W - 2 * M, h: 0.32, fontSize: 12, italic: true, color: C.text2 });

  // ================= Section: Status and plan =================
  section("03", "Where we are", "A working prototype, a pilot to pick, owners to name");

  // 16 Prototype numbers
  s = content("Where we are", "Built in a day against live sources");
  const st = [
    ["26,903", "entities", "from 1,485 PDSC files", C.accent5, fa.FaSitemap, HEX.deep],
    ["550", "knowledge units", "24 procedures, 120 rules, 397 error units", C.accent1, fa.FaLayerGroup, HEX.teal],
    ["3", "MCP tools", "search, get, expand", C.accent2, fa.FaPlug, HEX.copper],
    ["15/15", "tests pass", "stale check, context filter, MCP round trip", C.accent4, fa.FaVialCircleCheck, HEX.berry],
  ];
  for (let i = 0; i < 4; i++) {
    const x = M + i * 3.07;
    card(s, x, 1.5, 2.85, 4.2, C.background2, "stat " + i);
    await badge(s, st[i][4], x + 0.95, 1.85, 0.95, st[i][5], HEX.white, st[i][1]);
    txt(s, st[i][0], { x: x + 0.15, y: 3.0, w: 2.55, h: 0.95, fontSize: 40, bold: true, fontFace: "Arial", color: st[i][3], align: "center", valign: "middle" });
    txt(s, st[i][1], { x: x + 0.15, y: 3.95, w: 2.55, h: 0.45, fontSize: 17, bold: true, align: "center" });
    txt(s, st[i][2], { x: x + 0.25, y: 4.45, w: 2.35, h: 1.0, fontSize: 13, color: C.text2, align: "center" });
  }
  txt(s, "Prototype on 4 Oct 2026. All units are drafts until reviewed.", { x: M, y: 6.35, w: W - 2 * M, h: 0.32, fontSize: 12, italic: true, color: C.text2 });

  // 17 Domains
  s = content("Where we are", "What we write next: domains Pack Docs don't cover");
  const dom = [
    [["RTOS kernel", fa.FaGears], ["Error catalog", fa.FaBug], ["Memory and linker", fa.FaMemory], ["Fault analysis", fa.FaTriangleExclamation]],
    [["Optimization", fa.FaGaugeHigh], ["Test", fa.FaFlaskVial], ["Project management", fa.FaFolderTree]],
    [["Boot and update", fa.FaPowerOff], ["Security and CRA", fa.FaShieldHalved], ["Edge AI", fa.FaBrain], ["Trace and profiling", fa.FaWaveSquare]],
  ];
  const head = [["Priority 1", "Not in Pack Docs at all", C.text1, HEX.copper], ["Priority 2", "Requested by the team", C.accent1, HEX.ink], ["Priority 3", "Complementary, selection", C.accent3, HEX.ink]];
  for (let c = 0; c < 3; c++) {
    const x = M + c * 4.1;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 1.45, w: 3.85, h: 0.95, rectRadius: 0.1, fill: { color: head[c][2] }, line: { color: head[c][2] }, objectName: "prio " + c });
    txt(s, [{ text: head[c][0], options: { bold: true, fontSize: 19, breakLine: true } }, { text: head[c][1], options: { fontSize: 13 } }], { x: x + 0.25, y: 1.5, w: 3.4, h: 0.85, color: C.background1, valign: "middle" });
    for (let i = 0; i < dom[c].length; i++) {
      const y = 2.6 + i * 0.92;
      card(s, x, y, 3.85, 0.78, C.background2, "dom " + dom[c][i][0]);
      await badge(s, dom[c][i][1], x + 0.15, y + 0.11, 0.56, c === 0 ? HEX.copper : HEX.teal, HEX.white, dom[c][i][0]);
      txt(s, dom[c][i][0], { x: x + 0.9, y, w: 2.8, h: 0.78, fontSize: 15, bold: true, valign: "middle" });
    }
  }
  txt(s, "Full map in 03_wissensdomaenen.md. 140 sources mapped with license mode in 04_quellenliste.md.", { x: M, y: 6.4, w: W - 2 * M, h: 0.32, fontSize: 12, italic: true, color: C.text2 });

  // 18 Plan
  s = content("Where we are", "Seven steps. Skills retire only after a parallel run");
  const mp = [["Inventory", true], ["Entity graph", true], ["Decompose skills", true], ["Pilot domain", false], ["Parallel run", false], ["Retire skills", false], ["Operate", false]];
  const sw = (W - 2 * M) / 7;
  s.addShape(pres.shapes.LINE, { x: M + sw / 2, y: 2.45, w: sw * 6, h: 0, line: { color: C.accent3, width: 3 }, objectName: "timeline" });
  mp.forEach((m, i) => {
    const x = M + i * sw + sw / 2 - 0.45;
    s.addShape(pres.shapes.OVAL, { x, y: 2.0, w: 0.9, h: 0.9, fill: { color: m[1] ? C.accent1 : C.background1 }, line: { color: C.accent1, width: 2.5 }, objectName: "milestone " + i });
    txt(s, String(i + 1), { x, y: 2.0, w: 0.9, h: 0.9, fontSize: 22, bold: true, color: m[1] ? C.background1 : C.accent1, align: "center", valign: "middle" });
    txt(s, m[0], { x: M + i * sw + 0.05, y: 3.05, w: sw - 0.1, h: 0.6, fontSize: 15, bold: true, align: "center" });
  });
  card(s, M, 4.1, 5.9, 1.6, C.background2, "done");
  txt(s, [{ text: "Prototype exists", options: { bold: true, color: C.accent1, fontSize: 17, breakLine: true } }, { text: "Steps 1 to 3 run end to end. Still open: Stage 2 for 20 procedures and human review.", options: {} }],
    { x: M + 0.3, y: 4.3, w: 5.3, h: 1.6, fontSize: 15 });
  card(s, M + 6.2, 4.1, W - 2 * M - 6.2, 1.6, C.text1, "next");
  txt(s, [{ text: "Starts with today's decisions", options: { bold: true, color: C.accent6, fontSize: 17, breakLine: true } }, { text: "Pilot domain with golden set, then a feature flag next to the skills in the CDA.", options: {} }],
    { x: M + 6.5, y: 4.3, w: W - 2 * M - 6.8, h: 1.6, fontSize: 15, color: C.background1 });

  // 19 Decisions
  s = content("Where we are", "What we need to decide");
  const dec = [
    [fa.FaFlag, "Pilot domain", "Recommendation: error catalog. Easy to fill and to measure."],
    [fa.FaPlug, "Pack Docs interface", "How the KB and the existing Pack Docs system share context."],
    [fa.FaScaleBalanced, "Canonical rules", "Approve five proposed rules, name who writes them."],
    [fa.FaMicrochip, "NPU entities", "Add Ethos-U as a target type for Edge AI units."],
    [fa.FaGavel, "Legal review", "Keil KB export, Arm compiler guides, Learning Paths (CC BY-SA)."],
    [fa.FaUserCheck, "Domain owners", "One maintainer per domain, reviews routed by CI."],
  ];
  for (let i = 0; i < dec.length; i++) {
    const x = M + (i % 3) * 4.1, y = 1.45 + Math.floor(i / 3) * 2.5;
    card(s, x, y, 3.85, 2.25, i === 0 ? C.text1 : C.background2, "decision " + i);
    await badge(s, dec[i][0], x + 0.3, y + 0.3, 0.75, i === 0 ? HEX.copper : HEX.teal, HEX.white, dec[i][1]);
    txt(s, dec[i][1], { x: x + 1.25, y: y + 0.3, w: 2.45, h: 0.75, fontSize: 18, bold: true, valign: "middle", color: i === 0 ? C.background1 : C.text1 });
    txt(s, dec[i][2], { x: x + 0.3, y: y + 1.2, w: 3.3, h: 0.9, fontSize: 14, color: i === 0 ? C.background2 : C.text2 });
  }

  // 20 Close
  s = pres.addSlide({ masterName: "DARK", sectionTitle: "Where we are" });
  s.addText("Next steps", { placeholder: "title" });
  s.addText("Owners and dates set in this meeting", { placeholder: "sub" });
  const ns = ["Stage 2 refinement for the remaining 20 procedures, then review",
    "Write cause and fix for the 134 csolution errors, based on resolved GitHub issues",
    "Golden set for the pilot, measured against today's skills",
    "knowledge.db in the CDA behind a feature flag"];
  ns.forEach((n, i) => {
    s.addShape(pres.shapes.OVAL, { x: M, y: 5.0 + i * 0.5, w: 0.34, h: 0.34, fill: { color: C.accent2 }, line: { color: C.accent2 }, objectName: "next " + i });
    txt(s, String(i + 1), { x: M, y: 5.0 + i * 0.5, w: 0.34, h: 0.34, fontSize: 12, bold: true, color: C.background1, align: "center", valign: "middle" });
    txt(s, n, { x: M + 0.5, y: 4.98 + i * 0.5, w: 11.5, h: 0.4, fontSize: 16, color: C.background1, valign: "middle" });
  });

  // ================= Backup =================
  pres.addSection({ title: "Backup" });
  s = backup("Under the hood: one SQLite file");
  const tb = [["nodes", "id, kind, type, domain, title, summary, body, meta", "every entity and unit"], ["edges", "src, rel, dst, qual", "the graph, version ranges in qual"],
    ["nodes_fts", "FTS5 over title, summary, body, symptoms, triggers", "keyword search, exact errors"], ["nodes_vec", "sqlite-vec, 384 dim (bge-small)", "search by meaning"], ["unresolved", "src, key, value", "stale applies_to, fails CI"]];
  tb.forEach((r, i) => {
    const y = 1.45 + i * 1.0;
    card(s, M, y, W - 2 * M, 0.85, C.background1, "table " + i);
    txt(s, r[0], { x: M + 0.3, y, w: 2.2, h: 0.85, fontSize: 16, bold: true, fontFace: "Courier New", color: C.accent1, valign: "middle" });
    txt(s, r[1], { x: M + 2.6, y, w: 5.8, h: 0.85, fontSize: 13, fontFace: "Courier New", valign: "middle" });
    txt(s, r[2], { x: M + 8.6, y, w: 3.4, h: 0.85, fontSize: 14, color: C.text2, valign: "middle" });
  });
  txt(s, "26 MB with all 26,903 entities. Full rebuild about 3 minutes on CPU.", { x: M, y: 6.5, w: W - 2 * M, h: 0.32, fontSize: 12, italic: true, color: C.text2 });

  s = backup("Entity graph by type");
  s.addChart(pres.charts.BAR, [{ name: "Entities", labels: ["Device", "Component", "DocSection", "Pack", "Subfamily", "Family", "Board", "API", "Core"], values: [12618, 6390, 2991, 1827, 1536, 884, 534, 58, 29] }],
    Object.assign({ x: M, y: 1.4, w: 8.0, h: 5.3, barDir: "bar", chartColors: [HEX.deep], showValue: true, dataLabelPosition: "outEnd", dataLabelFontSize: 12, dataLabelColor: HEX.ink,
      catAxisLabelFontSize: 13, catAxisLabelColor: HEX.ink, valAxisHidden: true, valGridLine: { style: "none" }, catGridLine: { style: "none" }, showLegend: false, catAxisOrientation: "maxMin", barGapWidthPct: 45 }, chartText));
  card(s, M + 8.4, 1.5, W - 2 * M - 8.4, 5.0, C.background1, "entity notes");
  txt(s, [{ text: "Notes", options: { bold: true, fontSize: 17, breakLine: true } },
    { text: "Same component ID ships in many DFPs, so device or family is the better applies_to target.", options: { bullet: true, breakLine: true } },
    { text: "NPUs have no entity yet.", options: { bullet: true, breakLine: true } },
    { text: "3 vendor PDSC files are not valid XML.", options: { bullet: true } }], { x: M + 8.65, y: 1.75, w: 3.3, h: 4.5, fontSize: 14, paraSpaceAfter: 8 });

  s = backup("Error catalog pilot: where the work is");
  s.addChart(pres.charts.BAR, [
    { name: "Cause and fix documented", labels: ["packchk", "svdconv", "csolution"], values: [85, 129, 0] },
    { name: "Symptom only", labels: ["packchk", "svdconv", "csolution"], values: [36, 13, 134] }],
    Object.assign({ x: M, y: 1.4, w: 7.0, h: 5.2, barDir: "col", barGrouping: "stacked", chartColors: [HEX.teal, HEX.berry], showValue: true, dataLabelPosition: "ctr", dataLabelColor: HEX.white, dataLabelFontSize: 13, dataLabelFormatCode: "0;;;",
      catAxisLabelFontSize: 14, catAxisLabelColor: HEX.ink, valAxisHidden: true, valGridLine: { style: "none" }, showLegend: true, legendPos: "b", legendFontSize: 12, legendColor: HEX.ink, barGapWidthPct: 60 }, chartText));
  card(s, M + 7.4, 1.5, W - 2 * M - 7.4, 5.0, C.background1, "err notes");
  txt(s, [{ text: "Notes", options: { bold: true, fontSize: 17, breakLine: true } },
    { text: "packchk and svdconv READMEs document 214 messages (Apache-2.0).", options: { bullet: true, breakLine: true } },
    { text: "csolution: 134 messages, no docs. Cause and fix get written from resolved GitHub issues.", options: { bullet: true, breakLine: true } },
    { text: "M302 exists in packchk and svdconv. Tool context disambiguates.", options: { bullet: true } }], { x: M + 7.65, y: 1.75, w: 4.4, h: 4.5, fontSize: 14, paraSpaceAfter: 8 });

  s = backup("Sources and licensing");
  s.addChart(pres.charts.DOUGHNUT, [{ name: "Mode", labels: ["V: full text", "S: own summary + link", "R: reference only"], values: [67, 60, 13] }],
    Object.assign({ x: M, y: 1.4, w: 5.4, h: 5.2, holeSize: 58, chartColors: [HEX.teal, HEX.sea, HEX.copper], showPercent: false, showValue: true, dataLabelColor: HEX.white, dataLabelFontSize: 14, showLegend: true, legendPos: "b", legendFontSize: 13, legendColor: HEX.ink }, chartText));
  card(s, M + 5.9, 1.5, W - 2 * M - 5.9, 5.0, C.background1, "src notes");
  txt(s, [{ text: "140 sources, rules we work by", options: { bold: true, fontSize: 17, breakLine: true } },
    { text: "Every unit traces to a listed source or a named author.", options: { bullet: true, breakLine: true } },
    { text: "Open licenses indexed in full. Arm documents start at S.", options: { bullet: true, breakLine: true } },
    { text: "Learning Paths text is CC BY-SA 4.0: kept apart from the Apache-2.0 pack.", options: { bullet: true, breakLine: true } },
    { text: "Standards like MISRA only by rule number.", options: { bullet: true } }], { x: M + 6.15, y: 1.75, w: 5.9, h: 4.5, fontSize: 15, paraSpaceAfter: 8 });

  const out = "/home/claude/work/deck/CMSIS_Knowledge_Base_Kickoff.pptx";
  await pres.writeFile({ fileName: out });
  await applyTheme(out, THEME);
  console.log("written");
})();
