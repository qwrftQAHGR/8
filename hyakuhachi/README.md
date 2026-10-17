# HYAKUHACHI: The Hundred and Eight Threads

A setting bible and SillyTavern worldbook for a comedic, lewd, two-Japans yokai rom-com.

| Path | What it is |
|---|---|
| `bible/01–13*.md` | **The setting bible.** This is the single source of truth. Each `##` section becomes one worldbook entry. |
| `worldbook/hyakuhachi.json` | **The SillyTavern World Info file.** It is generated from the bible, and every entry is constant (always on). |
| `tools/build_worldbook.py` | Rebuilds the JSON from the bible: `python3 tools/build_worldbook.py` |
| `greeting.md` | An optional first message for a narrator card. It follows the Opening Scene checklist. |
| `00-pitch.md` | The original pitch (superseded, kept for history). |

## Editing
Edit only the bible, then rerun the build script. The JSON is a verbatim copy of every section, so nothing is lost. To add an entry, add a `## Heading` to any bible file. The bible uses `{{user}}` for the protagonist, and SillyTavern fills in the persona name.

## Importing into SillyTavern
1. Open World Info, choose **Import**, and select `worldbook/hyakuhachi.json`.
2. Activate it globally or bind it to the chat or character.
3. **Raise the World Info budget.** All entries total about 23k tokens. SillyTavern's default budget (a share of context) will drop entries, so set the budget high enough, or use a large-context model. Entries also carry `ignoreBudget: true` for builds that support it.
4. Entries are inserted *before character definitions* in bible order. The Narrator Guide comes last, which gives it the most weight.
