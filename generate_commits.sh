#!/bin/bash

start_date="2023-02-25"
end_date="2025-04-25"
total_commits=526
files=("wallet/main.py" "wallet/services/wallet_manager.py" "wallet/services/token_swap.py" "wallet/models/schema.py" "README.md")

generate_commit_message() {
  verbs=("Fix" "Add" "Improve" "Update" "Refactor" "Remove" "Optimize")
  objects=("wallet" "token swap" "balance fetch" "eth support" "L2 chain" "API route" "RPC config" "seed generation")
  contexts=("logic" "flow" "case" "interface" "security" "support")

  echo "${verbs[$RANDOM % ${#verbs[@]}]} ${objects[$RANDOM % ${#objects[@]}]} ${contexts[$RANDOM % ${#contexts[@]}]}"
}

touch dummy.log
git add .

for i in $(seq 1 $total_commits); do
  # рандомная дата в диапазоне
  days_range=$(( ( $(date -d "$end_date" +%s) - $(date -d "$start_date" +%s) ) / 86400 ))
  random_days=$((RANDOM % days_range))
  commit_date=$(date -d "$start_date +$random_days days" +%Y-%m-%dT%H:%M:%S)

  # правим один из файлов, чтобы были изменения
  echo "# $i" >> ${files[$RANDOM % ${#files[@]}]}
  
  git add .
  GIT_AUTHOR_DATE="$commit_date" GIT_COMMITTER_DATE="$commit_date" \
  git commit -m "$(generate_commit_message)"
done
