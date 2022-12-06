(defn parse-input [input]
  (let [elves []
        current-elf-calories []]
    (doseq [line (line-seq input)]
      (if (not (empty? line))
        (conj current-elf-calories (Integer/parseInt line))
        (do
          (conj elves current-elf-calories)
          (let [current-elf-calories []]))))
    elves))

(defn find-elf-with-most-calories [elves]
  (apply max-key #(reduce + %) elves))

(defn solve-challenge [input]
  (let [elves (parse-input input)
        elf-with-most-calories (find-elf-with-most-calories elves)]
    (println elf-with-most-calories)))

(with-open [reader (clojure.java.io/reader "/Users/lukaszsciga/projects/advent-of-code-2022/day1/first-input.txt")]
  (solve-challenge reader))