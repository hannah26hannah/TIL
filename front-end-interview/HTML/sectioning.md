# HTML Sectioning Elements

Many HTML sectioning like `main`, `nav`, `aside` elements by default define ARIA landmarks. If HTML sectioning elements are used without understanding the associated landmark structure, assistive technology users will most likely be confused and less efficient in accessing content and interacting with web pages.

|HTML Element|Default Landmark Role|
|--|--|
|`aside`|`complementary`|
|`footer`|`contentinfo` when in context of the `body` element. The `footer` element is not a `contentinfo` landmark when it is a descendant of the following HTML sectioning elements (`article, aside, main, nav, section`)|
|form|form when it has an accessible name using `aria-labelledby`, `aria-label` or `title` attributes|
|`header`|`banner` when in context of the `body` element. The `header` element is not a `banner` landmark when it is a descendant of the following HTML sectioning elements: (`article, aside, main, nav, section`)|
|`main`|`main`|
|`nav`|`navigation`|
|`section`|region when it has an accessible name using `aria-labelledby`, `aria-label` or `title` attribute|

