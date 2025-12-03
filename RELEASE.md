# Release Process

This document explains how releases work in this project using a **Git Flow** strategy with manual release triggering.

## Branch Strategy

We use a simplified Git Flow model with two main branches:

### Branches

- **`develop`**: Main development branch
  - All feature PRs merge here
  - Active development happens here
  - Protected (requires PR + passing CI)

- **`main`**: Production/release-only branch
  - Only release PRs merge here
  - Represents what's in production
  - Protected (requires PR + passing CI + reviews)

- **`release/X.Y.Z`**: Temporary release preparation branches
  - Created automatically by the release workflow
  - Contains version bumps and changelog updates
  - Gets merged to `main`, then merged back to `develop`

### Workflow Diagram

```
develop ──┬──> feature branches ──> PR ──> develop
          │
          └──> (manual trigger) ──> release/X.Y.Z ──> PR ──> main
                                                              │
                                                              └──> auto-merge ──> develop
```

## Versioning Strategy

We use **Semantic Versioning** (SemVer): `MAJOR.MINOR.PATCH`

- **MAJOR**: Breaking changes (e.g., removing operations, changing CLI syntax)
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes, documentation, CI improvements

Version bumps are determined automatically by analyzing **conventional commits** since the last release.

## Release Process

### Step 1: Develop Features

Work on the `develop` branch as usual:

```bash
# Create feature branch from develop
git checkout develop
git pull
git checkout -b feature/my-feature

# Make changes and commit
git commit -m "feat: add new calculator operation"

# Create PR to develop
git push -u origin feature/my-feature
# Open PR: feature/my-feature → develop
```

### Step 2: Trigger Release (Manual)

When ready to release, trigger the **Create Release** workflow manually:

1. Go to GitHub Actions → "Create Release" workflow
2. Click "Run workflow"
3. Select branch: **`develop`** (required)
4. Choose release type:
   - **auto** (default): Analyzes commits to determine version bump
   - **patch**: Force patch version bump (0.2.0 → 0.2.1)
   - **minor**: Force minor version bump (0.2.0 → 0.3.0)
   - **major**: Force major version bump (0.2.0 → 1.0.0)

The workflow will:
- Analyze commits since last release
- Determine next version (based on conventional commits or your selection)
- Create `release/X.Y.Z` branch from `develop`
- Update `pyproject.toml` with new version
- Update `CHANGELOG.md` with categorized changes
- Create a PR: `release/X.Y.Z` → `main`

### Step 3: Review Release PR

Review the automatically created release PR:

- ✅ Verify version bump is correct
- ✅ Review CHANGELOG.md updates for accuracy
- ✅ Ensure all changes are properly categorized
- ✅ Check for breaking changes
- ✅ Confirm CI passes

### Step 4: Merge to Finalize Release

When the release PR is approved and CI passes, **merge it to `main`**.

The **Finalize Release** workflow will automatically:

1. Create git tag (e.g., `v1.0.0`)
2. Push tag to GitHub
3. Create GitHub release with changelog
4. Build macOS arm64 binary
5. Attach binary to release
6. **Merge `main` back to `develop`** to keep branches in sync

That's it! The release is now live.

## Commit Message Format

Use **Conventional Commits** format for automatic version detection:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

### Commit Types and Version Bumps

| Type       | Version Bump | Example                                    |
|------------|--------------|-------------------------------------------|
| `feat:`    | MINOR        | `feat: add sqrt operation`                |
| `fix:`     | PATCH        | `fix: handle negative numbers in average` |
| `perf:`    | PATCH        | `perf: optimize division algorithm`       |
| `docs:`    | PATCH        | `docs: add usage examples`                |
| `ci:`      | PATCH        | `ci: add windows build`                   |
| `refactor:`| PATCH        | `refactor: simplify CLI parsing`          |
| `test:`    | PATCH        | `test: add edge case tests`               |
| `chore:`   | PATCH        | `chore: update dependencies`              |
| `style:`   | PATCH        | `style: format code with ruff`            |
| `build:`   | PATCH        | `build: update build process`             |

### Breaking Changes (MAJOR bump)

Add `BREAKING CHANGE:` in commit footer or `!` after type:

```
feat!: change CLI syntax to use flags

BREAKING CHANGE: Operations now require --op flag instead of positional argument
```

Or:

```
refactor: redesign calculator API

BREAKING CHANGE: Calculator class constructor signature changed
```

## Examples

### Scenario 1: New Feature Release

```bash
# On develop branch
git commit -m "feat: add power operation

Adds pow operation to calculator.
Supports both integer and float exponents.
Includes comprehensive tests."

git push

# Trigger release workflow from GitHub UI
# Select: branch=develop, release-type=auto
# Result: Creates release/0.3.0 → main PR
# After merge: v0.3.0 released, changes merge back to develop
```

### Scenario 2: Bug Fix Release

```bash
# On develop branch
git commit -m "fix: prevent divide by zero in average

Previously average([]) would crash.
Now returns 0.0 as expected."

git push

# Trigger release workflow
# Result: Creates release/0.2.1 → main PR (patch bump)
```

### Scenario 3: Multiple Changes

```bash
# Multiple commits on develop
git commit -m "feat: add logarithm operation"
git commit -m "fix: improve error messages"
git commit -m "docs: update API documentation"
git push

# Trigger release workflow
# Result: MINOR bump (0.2.0 → 0.3.0) because of "feat:"
# CHANGELOG will include all three changes under appropriate sections
```

### Scenario 4: Force Specific Version

Sometimes you want to control the version bump manually:

```bash
# Trigger release workflow with release-type=major
# Even if commits suggest minor/patch, this forces 1.0.0
```

## Current Version Scheme

- **0.x.x**: Pre-1.0 development phase (current)
- **1.0.0**: First stable release (when API/CLI is stable)
- **1.x.x**: Post-1.0 following strict SemVer

## Troubleshooting

### Workflow says "No release needed"

The `develop` branch has no new releasable commits since the last release. Commits must use conventional commit format:

```bash
# ✅ Will be included in release
git commit -m "feat: add new feature"
git commit -m "fix: correct bug"

# ❌ Won't trigger version bump (but should still use conventional format!)
git commit -m "ci: update workflow"  # Patch bump
git commit -m "chore: reorganize code"  # Patch bump
```

**All commits should follow conventional format**, even if they're just chores.

### Release PR fails CI

The release branch is created from `develop`, so if `develop` has failing tests, the release PR will also fail. Fix the issues on `develop` first, then re-trigger the release.

### Wrong version bump

**Option 1**: Close the release PR without merging, and re-trigger the workflow with a different `release-type` (patch/minor/major).

**Option 2**: Manually edit `pyproject.toml` and `CHANGELOG.md` in the release PR before merging.

### Need to undo a release

```bash
# 1. Delete the tag
git tag -d v0.3.0
git push --delete origin v0.3.0

# 2. Delete GitHub release in web UI

# 3. Revert the merge commit on main
git checkout main
git revert -m 1 <merge-commit-hash>
git push

# 4. Update develop to match
git checkout develop
git merge main
git push
```

### Merge conflicts between main and develop

This shouldn't happen often if you:
- Always create releases from `develop`
- Let the workflow merge main back to develop automatically

If it does happen:
```bash
git checkout develop
git pull
git merge main
# Resolve conflicts
git commit
git push
```

## Branch Protection Setup

Recommended settings:

### `main` branch:
- ✅ Require pull request before merging
- ✅ Require approvals: 1
- ✅ Require status checks to pass: `lint`, `test (3.10)`, `test (3.11)`, `test (3.12)`
- ✅ Require conversation resolution before merging
- ❌ Do NOT allow bypassing (keep releases manual)

### `develop` branch:
- ✅ Require pull request before merging
- ✅ Require status checks to pass: `lint`, `test (3.10)`, `test (3.11)`, `test (3.12)`
- ✅ Require conversation resolution before merging

## See Also

- [Keep a Changelog](https://keepachangelog.com/)
- [Semantic Versioning](https://semver.org/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [python-semantic-release docs](https://python-semantic-release.readthedocs.io/)
- [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/)
