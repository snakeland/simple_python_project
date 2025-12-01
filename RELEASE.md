# Release Process

This document explains how releases work in this project.

## Versioning Strategy

We use **Semantic Versioning** (SemVer): `MAJOR.MINOR.PATCH`

- **MAJOR**: Breaking changes (e.g., removing operations, changing CLI syntax)
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes, documentation, CI improvements

## Automated Releases

Releases are **semi-automated** using `python-semantic-release` based on conventional commits. The process creates a release PR that requires manual review and approval before the release is finalized.

### How It Works

The release process has two main stages:

#### Stage 1: Release PR Creation (Automated)

When you **commit with conventional format** to `main` branch:
```bash
feat: add new operation     # Triggers MINOR version bump
fix: correct calculation    # Triggers PATCH version bump
docs: update README         # Triggers PATCH version bump
```

The **Semantic Release workflow** automatically:
- Analyzes commits since last release
- Determines version bump (major/minor/patch)
- Updates `version` in `pyproject.toml`
- Updates `CHANGELOG.md`
- Creates a release PR (e.g., `chore(release): 0.3.0`)

#### Stage 2: Release Finalization (Manual Review Required)

1. **Review the release PR** created by the workflow:
   - Verify the version bump is correct (check `pyproject.toml`)
   - Review the CHANGELOG.md updates for accuracy
   - Ensure all changes are properly categorized
   - Check that breaking changes are clearly marked

2. **Merge the release PR** to trigger finalization:
   - The `finalize-release` job automatically runs
   - Creates git tag (e.g., `v0.3.0`)
   - Pushes tag to GitHub
   - Creates GitHub release with changelog

3. **Build workflow** automatically:
   - Builds macOS arm64 binary
   - Attaches binary to the GitHub release

## Commit Message Format

Use conventional commits format:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

### Types that trigger releases:

| Type       | Version Bump | Example                                    |
|------------|--------------|-------------------------------------------|
| `feat:`    | MINOR        | `feat: add sqrt operation`                |
| `fix:`     | PATCH        | `fix: handle negative numbers in average` |
| `perf:`    | PATCH        | `perf: optimize division algorithm`       |
| `docs:`    | PATCH        | `docs: add usage examples`                |
| `ci:`      | PATCH        | `ci: add windows build`                   |
| `refactor:`| PATCH        | `refactor: simplify CLI parsing`          |
| `test:`    | PATCH        | `test: add edge case tests`               |

### Breaking changes (MAJOR bump):

Add `BREAKING CHANGE:` in commit footer or `!` after type:

```
feat!: change CLI syntax to use flags

BREAKING CHANGE: Operations now require --op flag instead of positional argument
```

## Manual Release (Alternative)

If you prefer manual control, you can use the `release.yml` workflow:

1. Update version in `pyproject.toml`
2. Update `CHANGELOG.md`
3. Commit changes
4. Create and push tag:
   ```bash
   git tag v0.3.0
   git push --tags
   ```
5. The `release.yml` workflow will create the GitHub release

## Current Version Scheme

- **0.x.x**: Pre-1.0 development phase (we are here)
- **1.0.0**: First stable release (when CLI is stable and documented)
- **1.x.x**: Post-1.0 following strict SemVer

## Examples

### Adding a new feature
```bash
git commit -m "feat: add power operation for exponentiation

Adds pow operation to calculator with CLI alias.
Supports both integer and float exponents."

# This will trigger:
# - Semantic Release workflow creates a PR titled "chore(release): 0.3.0"
# - The PR contains:
#   - Version bump: 0.2.0 → 0.3.0 in pyproject.toml
#   - CHANGELOG update with "Added" section
# - After PR is reviewed and merged:
#   - GitHub release v0.3.0 is created
#   - macOS binary is built and attached
```

### Fixing a bug
```bash
git commit -m "fix: prevent divide by zero crash in average

Previously average([0, 0, 0]) would crash.
Now returns 0.0 as expected."

# This will trigger:
# - Semantic Release workflow creates a PR titled "chore(release): 0.2.1"
# - The PR contains:
#   - Version bump: 0.2.0 → 0.2.1 in pyproject.toml
#   - CHANGELOG update with "Fixed" section
# - After PR is reviewed and merged:
#   - GitHub release v0.2.1 is created
#   - macOS binary is built and attached
```

### Documentation only (still creates patch release)
```bash
git commit -m "docs: add installation instructions to README"

# This will trigger:
# - Semantic Release workflow creates a PR titled "chore(release): 0.2.1"
# - The PR contains:
#   - Version bump: 0.2.0 → 0.2.1 in pyproject.toml
#   - CHANGELOG update
# - After PR is reviewed and merged:
#   - GitHub release v0.2.1 is created
#   - macOS binary is built and attached
```

## Skipping Releases

To commit without triggering a release, use:

```bash
git commit -m "chore: update development notes

[skip ci]"
```

Note: The following commit types **do** trigger patch releases in this project:
- `chore:` - Maintenance tasks
- `style:` - Code formatting (no logic changes)
- `build:` - Build system changes

To avoid triggering a release for these commit types, add `[skip ci]` to your commit message.
## Troubleshooting

### Release PR not created
- Check that commit is on `main` branch
- Verify commit message follows conventional format
- Check GitHub Actions workflow run for errors
- Ensure no previous release PR is already open

### Release PR created but no release after merge
- Check that the PR title starts with `chore(release):`
- Verify the `finalize-release` job ran successfully
- Check GitHub Actions workflow logs for errors

### Wrong version bump
- Review the release PR before merging
- Check that commit types are correct (`feat:` vs `fix:`)
- For breaking changes, ensure `BREAKING CHANGE:` footer or `!` after type
- Close the PR without merging and fix the original commits if needed

### Need to undo a release
```bash
# Delete tag locally and remotely
git tag -d v0.3.0
git push --delete origin v0.3.0

# Delete GitHub release manually in web UI
# Revert the version commit
git revert <commit-hash>
```

## See Also

- [Keep a Changelog](https://keepachangelog.com/)
- [Semantic Versioning](https://semver.org/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [python-semantic-release docs](https://python-semantic-release.readthedocs.io/)
