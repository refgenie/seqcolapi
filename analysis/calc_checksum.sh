for f in `ls data/*.fa.gz`; do
  echo "Calculating checksum for ${f}"
  checksumseq --input ${f} --output ${f}.checksums
done