CSS is a language that can be used to add style to an [HTML](/wiki/HTML) page.

Cascading Style Sheets (CSS) is a style sheet language used for describing the presentation of a document written in a markup language such as *HTML*. CSS is a cornerstone technology of the World Wide Web, alongside *HTML* and *JavaScript*.

The CSS specifications are maintained by the World Wide Web Consortium (W3C). Internet media type (MIME type) `text/css` is registered for use with CSS by **RFC 2318** (March 1998). The W3C operates a free CSS validation service for CSS documents.

# Syntax
CSS has a simple syntax and uses a number of English keywords to specify the names of various style properties.

A style sheet consists of a list of rules. Each rule or rule-set consists of one or more selectors, and a declaration block.

## Selector
In CSS, selectors declare which part of the markup a style applies to by matching tags and attributes in the markup itself.

Selectors may apply to the following:

- all elements of a specific type, e.g. the second-level headers h2
- elements specified by attribute, in particular:
   - id: an identifier unique within the document, identified with a hash prefix e.g. #id
   - class: an identifier that can annotate multiple elements in a document, identified with a period prefix e.g. .classname
- elements depending on how they are placed relative to others in the document tree.

For example, under pre-CSS HTML, a heading element defined with red text would be written as:

```
<style>
    h1 {
        color: red;
    }
</style>
```

### Example
Given the following style sheet:

```
h1 {
   color: pink;
}
```

Suppose there is an h1 element with an emphasizing element (em) inside.
If no color is assigned to the em element, the emphasized word "illustrate" inherits the color of the parent element, h1. The style sheet h1 has the color pink, hence, the em element is likewise pink.