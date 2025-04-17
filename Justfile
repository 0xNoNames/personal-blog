[no-cd]
default:
  - hugo serve -D -buildFuture -buildDrafts

pull:
  - cd content/articles && git pull
