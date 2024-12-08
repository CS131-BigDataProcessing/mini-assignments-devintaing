process allCaps {
  input:
  val(input) from params.str

  script:
  """
  allCaps = input.toUpperCase()
  println("$allCaps")
  """
}

workflow {
  allCaps()
}