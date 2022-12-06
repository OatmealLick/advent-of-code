(ns app)

(defn DoGroup [coll item] (conj (drop-last coll) (conj (last coll) item)))

(defn Group [l]
  (reduce
   (fn [coll item] 
     (if (== item 2) 
       (conj coll [])
       (DoGroup coll item)))
   [[]]
   l))
(Group [1 2 3 4 5 2 9])

(defn Example []
  (with-open [rdr (clojure.java.io/reader "/Users/lukaszsciga/projects/advent-of-code-2022/day1/first-input.txt")]
    (reduce () [] (reduce conj [] (line-seq rdr)))))

(Example)

[[1] [3 4]] 5