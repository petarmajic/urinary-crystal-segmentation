# Original layout and provenance

The source snapshot is commit `b50814d20c459f4cde0f95a62ad481d524dd7fe4`. All substantive original files retain their Git blob identities. The [migration map](migration-map.csv) records every original path, current location, blob SHA and size.

The structure preserves **1,962 original file blobs**, including both supplied notebook copies and both copies of the specification. Sixteen incidental files (OS metadata and an Office lock file) are excluded from the new tree. The old root title and inherited GitLab README are retained here as `original-root-readme.md` and `original-gitlab-readme.md`.

The top-level [`notebooks/PRI_train.ipynb`](../../notebooks/PRI_train.ipynb) is the canonical notebook link. The [report specification](../reports/project-specification.pdf) is the canonical specification link. Their identical supplied copies remain in the relevant archive subdirectories.

Raw images and annotation files retain their contents and internal hierarchy under `data/raw/` and `data/annotated/`. Folder moves do not reduce Git history size. Original source code still contains historical paths; [execution notes](../reproducibility.md) explain what needs adaptation before a new run.
