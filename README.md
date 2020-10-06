name: GitHub Stats with WakaTime
on:
  schedule:
    # Runs at 12am IST
    - cron: '30 18 * * *'
jobs:
  update-readme:
    name: Update Readme with Metrics
    runs-on: ubuntu-latest
    steps:
      - uses: SRagavendar/GitHub_Stats@master
        with:
          WAKATIME_API_KEY: ${{ secrets.4082c212-ebe2-4a72-b360-47baa08fac9c }}
          GH_TOKEN: ${{ secrets.b7ff3e3c5a8d75fc125e933641025674d91dd846 }}
          SHOW_COMMIT: "True"
          SHOW_LANGUAGE: "True"
          SHOW_EDITORS: "True"
          SHOW_TIMEZONE: "True"