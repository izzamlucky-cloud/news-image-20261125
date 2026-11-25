// News Image entry for make.fun, Wednesday 25 November 2026.
// The program copies the image held in this repository to the
// grader's output directory. Node 22, standard library only, no
// network, and deterministic: the same bytes go out every run.
// entry.png is 1024x1024, drawn for this day's news.

import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const source = new URL('./entry.png', import.meta.url);
const target = join(outputDir, 'entry.png');

mkdirSync(outputDir, { recursive: true });
copyFileSync(source, target);
