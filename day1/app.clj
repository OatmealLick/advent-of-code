(ns app)

(defn Group)

(defn Example []
  (with-open [rdr (clojure.java.io/reader "/Users/lukaszsciga/projects/advent-of-code-2022/day1/first-input.txt")]
    
    
    (reduce () [] (reduce conj [] (line-seq rdr)))
    
    
    ))

(Example)
