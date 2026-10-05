#!/usr/bin/env node
/*
 * Retrieval check with the extension's own search: tests/golden.json against a knowledge.db.
 *
 * Usage: node tests/eval_search.js <knowledge.db> <checkout of CMSIS-Developer-Assistant> [--k=5] [--verbose]
 * The checkout must be compiled (npm run compile), the search is taken from its out/ folder.
 * Prints hit@1, hit@k and MRR, and every miss. Exits 1 when a query marked top1 is not first,
 * or when an expected id is not in the index (a renamed unit).
 */
const path = require('path');
const fs = require('fs');

const args = process.argv.slice(2).filter((a) => !a.startsWith('--'));
const flags = process.argv.slice(2).filter((a) => a.startsWith('--'));
if (args.length !== 2) {
    console.error('usage: node tests/eval_search.js <knowledge.db> <CMSIS-Developer-Assistant checkout> [--k=5] [--verbose]');
    process.exit(2);
}
const [dbFile, cda] = args;
const k = Number((flags.find((f) => f.startsWith('--k=')) || '--k=5').slice(4));
const verbose = flags.includes('--verbose');
const out = path.resolve(cda, 'out', 'src', 'core', 'knowledge');
const { KnowledgeIndex } = require(path.join(out, 'store.js'));
const { contextEntities, searchKnowledge } = require(path.join(out, 'search.js'));

const golden = JSON.parse(fs.readFileSync(path.join(__dirname, 'golden.json'), 'utf8')).queries;
const index = new KnowledgeIndex(path.resolve(dbFile));

let hit1 = 0;
let hitK = 0;
let rr = 0;
let failed = 0;
for (const g of golden) {
    const missing = g.expect.filter((id) => index.node(id) === undefined);
    if (missing.length > 0) {
        console.log(`MISSING  ${missing.join(', ')}  (query: ${g.q.split('\n')[0]})`);
        failed++;
        continue;
    }
    const context = g.tools ? contextEntities(index, { tools: g.tools }) : undefined;
    const ids = searchKnowledge(index, g.q, { k: Math.max(k, 10), budgetTokens: 100000, context }).results.map((r) => r.id);
    const rank = ids.findIndex((id) => g.expect.includes(id));
    if (rank === 0) {
        hit1++;
    }
    if (rank >= 0 && rank < k) {
        hitK++;
    }
    if (rank >= 0) {
        rr += 1 / (rank + 1);
    }
    const bad = rank !== 0 && g.top1;
    if (bad) {
        failed++;
    }
    if (bad || rank < 0 || rank >= k || verbose) {
        const mark = bad ? 'FAIL' : rank === 0 ? 'ok  ' : rank < 0 || rank >= k ? 'miss' : 'low ';
        console.log(`${mark}  #${rank < 0 ? '-' : rank + 1}  ${g.q.split('\n')[0].slice(0, 70)}\n        got ${ids.slice(0, 3).join(', ')}`);
    }
}
const n = golden.length;
console.log(`\n${n} queries  hit@1 ${(hit1 / n).toFixed(2)}  hit@${k} ${(hitK / n).toFixed(2)}  MRR ${(rr / n).toFixed(3)}  failures ${failed}`);
process.exit(failed > 0 ? 1 : 0);
