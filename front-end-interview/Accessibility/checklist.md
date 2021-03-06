# ✔ CheckList

# Content
- Use Plain language and avoid figures of speech, idioms, and complicated metaphors.
- Make sure that `button`, `a`, and `label` element content is unique and descriptive
- Use left-aligned text for left-to-right (LTR) languages, and right-aligned text for right-to-left (RTL) languages.

# Global Code
means code that affects your entire website or web app.

- Validate your HTML
    : helps to provide an consistent, expected experience across all browsers and assistive technoloty. 
- Use a lang attribute on the html element.
    : This helps assistive technology such as screen readers to pronounce content correctly. 
- Provide a unique title for each page or view
    : The `title` element, contained in the document's `head` element, is often the first piece of information announced by assistive techonology. This helps tell peiplpe what page or view they are going to start navigating.
- Ensure that viewport zoom is not disabled.
    : Some people need to increase the size of text to a point where they can read it. Do not stop them from doing this, even for web apps with a native app-like experience. Even native apps should respect Operating System settings for resizing text.
- Use landmark elements to indicate important content regions.
    : Landmark regions help communicate the layout and important areas of a page or view, and can allow quick access to these regions. For example, use the `nav` element to wrap a site's navigation, and the `main` element to containes the primary content of a page.
    [HTML Sectioning Elements](../HTML/sectioning.md)
- Ensure a linear content flow
    : Remove `tabindex` attribute values that aren't either `0` or `-1`. Elements that are inherently focusable, such as links or `button` elements, do not require a `tabindex`. Elements that are not inherently focusable should not have a tabindex applied to them outside of very specified use cases.
- Avoid using the `autofocus` attribute
    : People who are blind or who have low vision may be disoriented when focus is moved without their permission. Additionally, `autofocus` can be problematic for people with motor control disabilities, as it may create extra work for them to navigate out from the autofocused area and to other location on the page/view
- Remove session timeouts
    : if you can't, let person using your site know the timeout exists ahead of time, and provide significant notice before the timer runs out.
- Remove `title` attribute tooltips
    : The title attribute has numerous issues, and should not be used if the information provided is important for all people who access. An accepatable use for the `title` attribute would be labeling an `iframe` element to indicate what content it contains.

# Keyboard
It's important that your interface and content can be operated and navigated by use of keyboard. Some poeple can't use a mouse or may be suing other assitive techonologies that may not allow for hovering or precise clicking.

- Make sure there is a visibile focus style for interactive elements that are navigated to via keyboard input. 
    : Can a person navigating with a keyboard, switch, voice control, or screen reader see where they currently are on the page?
- Check to see that keyboard focus order matches the visual layout.
    : Can a person navigating with a keyboard or screen reader move around the page in a predictable way?
- Remove invisible focusable elements
    : Remove the ability to focus on elements that are not presently meant to be discoverable. This includes things like inactive drop down menus, off screen navigations or modals.

# Images
Images are a very common part of most websites. Help make sure they can be enjoyed by all.

- Make sure that all `img` elements have an `alt` attributes.

..

# Headings
Heading elements (h1, h2, h3.. ) help break up the content of the page into related 'chunks' of information. They are incredibly important for helping people who use assitive technology to understand the meaning of a page or view.

# Lists
Lists elements let people know a collection of items are related and if they are sequential, and how many items are present in the list grouping.

# Controls
Controls are interactive elements such as links and buttons that let people navigate to a destination or perform an action.
- Use the `a` element for links.
- Ensure that links are recognizable as links.
- Ensure that controls have `:focus` states.
- Use the `button` element for button.
- Provide a skip link and make sure that it is vibile when focused.
- Identify links that open in a new tab or window

# Tables
Tables are a structred set of data that help people understand the relationships between different types of information.

# Forms
# Media
# Video
# Audio
# Appearance
# Animation
# Color Contrast
# Mobile/Touch


# Reference
[The A11y Project](https://www.a11yproject.com/checklist/)
[ARIA Landmarks Example](https://www.w3.org/TR/wai-aria-practices/examples/landmarks/HTML5.html)